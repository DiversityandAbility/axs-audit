import csv
import time
import json
import uuid
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlparse, urlsplit, urlunsplit, urljoin

from playwright.sync_api import sync_playwright, TimeoutError

from audit import ask
from audit.criteria import all_ as criteria

CRAWLED_URLS = set()


def crawl(browser, site, page, url):
    print(f"Found page: {url}")
    run_instructions(page, site["on_load"])
    yield page
    CRAWLED_URLS.add(url)

    if len(CRAWLED_URLS) == site["page_limit"]:
        return

    parent_url = urlparse(url)

    links = page.locator("a").element_handles()
    for link in links:
        href = link.get_attribute("href")
        href = urljoin(url, href)

        # Remove fragment & query parameter
        href = urlunsplit(urlsplit(href)._replace(query="", fragment=""))
        link_url = urlparse(href)

        if href in CRAWLED_URLS:
            continue

        if link_url.netloc != parent_url.netloc:
            continue

        child_page = browser.new_page()
        child_page.goto(href)
        yield from crawl(browser, site, child_page, href)
        child_page.close()

        if len(CRAWLED_URLS) == site["page_limit"]:
            return


def test(site, results_path, page, id_):
    for viewport in site["viewports"]:
        page.set_viewport_size(viewport)
        page.reload()
        ask.init(page)
        run_instructions(page, site["on_load"])
        page.screenshot(
            path=results_path / f"screenshots/page-{id_}-{viewport['name']}.png",
            full_page=True,
        )
        for C in criteria:
            c = C()
            print(f"{c.level}{c.name} - {c.summary}")
            for elem in c.find_elements(page):
                for tech_result in c.test(elem):
                    yield from tech_result.results


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


def main(details_path):
    try:
        with open(details_path, "r") as fp:
            site = json.load(fp)
    except FileNotFoundError:
        path = Path("audit") / "examples" / "small.json"
        with path.open("r") as fp:
            site = json.load(fp)
        site["seeds"][0][0][1] = details_path
    report_id = str(int(time.time()))
    print(f"Report ID: {report_id}")
    results_path = Path("results") / site["id"] / report_id
    results_path.mkdir(parents=True)
    details = {"started_on": datetime.now(timezone.utc).isoformat()}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        browser_context = browser.new_context()

        with open(results_path / "results.csv", "w") as fp:
            results_csv = csv.DictWriter(
                fp,
                fieldnames=[
                    "id",
                    "page",
                    "element",
                    "type",
                    "code",
                    "description",
                    "screenshot",
                ],
            )
            results_csv.writeheader()
            page_count = 0
            result_count = 0
            for seed_instructions in site["seeds"]:
                seed_page = browser_context.new_page()
                seed_page.add_init_script(path="audit/browser/finder.js")
                run_instructions(seed_page, seed_instructions)

                print(f"Starting seed: {seed_page.url}")
                for page in crawl(browser_context, site, seed_page, seed_page.url):
                    page_count += 1
                    page_id = str(uuid.uuid4())
                    print(f"\nPage ID: {page_id}")
                    screenshots = {}
                    for result in test(site, results_path, page, page_id):
                        result_count += 1
                        print(f"\n{result}")
                        d = result.as_dict()
                        d["page"] = page.url
                        d["screenshot"] = screenshots.get(d["element"], None)
                        if d["screenshot"] is None:
                            try:
                                p = (
                                    results_path
                                    / "screenshots"
                                    / f"issue-{result.id_}.png"
                                )
                                result.element.screenshot(path=p)
                                d["screenshot"] = p
                                screenshots[d["element"]] = p
                            except TimeoutError:
                                pass
                        results_csv.writerow(d)

                seed_page.close()

        print("")
        print(f"Looked at {page_count} pages")
        print(f"Found {result_count} results")

        details["finished_on"] = datetime.now(timezone.utc).isoformat()
        with open(results_path / "details.json", "w") as fp:
            json.dump(details, fp)

        browser_context.close()
        browser.close()
