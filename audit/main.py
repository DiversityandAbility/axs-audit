import time
import json
import uuid
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlparse, urlsplit, urlunsplit, urljoin

from playwright.sync_api import sync_playwright, TimeoutError

from audit.criteria import all_ as criteria


def screenshot(context, elem, **kwargs):
    id = str(uuid.uuid4())
    path = Path(context["results_path"]) / "screenshots" / f"{id}.png"
    try:
        elem.screenshot(path=path, **kwargs)
    except TimeoutError:
        return "screenshot failed"
    return id


def crawl(context, browser, url):
    print(f"Found page: {url}")
    page = browser.new_page()
    hrefs = set()
    context["results"][url] = {"screenshots": {}, "results": []}
    for viewport in context["viewports"]:
        page.set_viewport_size(viewport)
        resp = page.goto(url)
        run_instructions(page, context["on_load"])
        sid = screenshot(context, page, full_page=True)
        context["results"][url]["screenshots"][f"page-{viewport['name']}"] = sid
        yield page, resp
        context["crawled_urls"].add(url)

        if len(context["crawled_urls"]) == context["page_limit"]:
            return

        parent_url = urlparse(url)

        # TODO: Work out how we could crawl sites using other than <a>
        #       e.g. <form> submission?
        #       e.g. weird JS page with lots of onclick?
        hrefs |= set(
            a.get_attribute("href") for a in page.locator("a").element_handles()
        )
    page.close()

    for href in hrefs:
        # Make sure href is absolute, doesn't not change domain etc. only adds the missing bits
        href = urljoin(url, href)

        # Remove fragment & query parameter
        href = urlunsplit(urlsplit(href)._replace(query="", fragment=""))
        link_url = urlparse(href)

        if href in context["crawled_urls"]:
            continue

        if link_url.netloc != parent_url.netloc:
            # If different domain/port/user don't crawl
            continue

        yield from crawl(context, browser, href)

        if len(context["crawled_urls"]) == context["page_limit"]:
            return


def test(context, page, resp):
    for C in criteria:
        print(f"  {C.ref} - {C.name} ({C.level}) - {C.summary}")
        test_context = {
            "answers": context["answers"],
            "request": resp.request,
            "response": resp,
        }
        for result in C().test(page, test_context):
            print(f"    {result}")
            sid = screenshot(context, getattr(result, "element", page))
            context["results"][page.url]["screenshots"][f"result-{result.id_}"] = sid
            context["results"][page.url]["results"].append(result.as_dict())
            yield result


def run_instructions(page, instructions):
    for action, value in instructions:
        if action == "goto":
            page.goto(value)
        if action == "click":
            page.click(value)
        elif action == "wait-for-load-state":
            page.wait_for_load_state(value)
        elif action == "wait-for-timeout":
            page.wait_for_timeout(1000)
        elif action == "lazy-scroll":
            if value == "bottom":
                page.mouse.move(100, 100)
                prev_height = None
                curr_height = page.evaluate("(window.innerHeight + window.scrollY)")
                while prev_height != curr_height:
                    prev_height = curr_height
                    page.mouse.wheel(0, 500)
                    page.wait_for_timeout(100)
                    curr_height = page.evaluate("(window.innerHeight + window.scrollY)")
                page.evaluate("() => window.scrollTo(0, 0)")


def main(context_or_url):
    report_id = str(int(time.time()))
    print(f"Report ID: {report_id}")

    try:
        with open(context_or_url, "r") as fp:
            context = json.load(fp)
    except FileNotFoundError:
        path = Path("audit") / "examples" / "small.json"
        with path.open("r") as fp:
            context = json.load(fp)
        context["seeds"][0][0][1] = context_or_url
        context["id"] = report_id
    context["crawled_urls"] = set()
    context["report_id"] = report_id
    context["started_on"] = datetime.now(timezone.utc).isoformat()

    results_path = Path("results") / context["id"] / report_id
    results_path.mkdir(parents=True)
    context["results_path"] = str(results_path)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        browser_context = browser.new_context()

        page_count = 0
        result_count = 0
        for seed_instructions in context["seeds"]:
            seed_page = browser_context.new_page()
            seed_page.add_init_script(path="audit/browser/finder.js")
            run_instructions(seed_page, seed_instructions)

            print(f"Starting seed: {seed_page.url}")
            for page, resp in crawl(context, browser_context, seed_page.url):
                page_count += 1
                for _ in test(context, page, resp):
                    result_count += 1

            seed_page.close()

        context["finished_on"] = datetime.now(timezone.utc).isoformat()
        with open(results_path / "context.json", "w") as fp:
            context["crawled_urls"] = list(context["crawled_urls"])
            json.dump(context, fp)

        print("")
        print(f"Looked at {page_count} pages")

        # TODO: Quick summary of result counts

        browser_context.close()
        browser.close()
