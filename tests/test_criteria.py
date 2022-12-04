import pytest
from bs4 import BeautifulSoup
from audit.criteria import all_ as criteria


@pytest.mark.parametrize(
    "criteria, good_html",
    [(c, good_html) for c in criteria for good_html in c.EXAMPLES_PASS],
)
def test_criteria_pass(page, criteria, good_html):
    page.set_content(f"<html><body>{good_html}</body></html>")
    soup = BeautifulSoup(page.content(), "html5lib")
    results = list(criteria.test(page, soup))
    assert len(results) == 0


@pytest.mark.parametrize(
    "criteria, bad_html, code",
    [(c, bad_html, code) for c in criteria for bad_html, code in c.EXAMPLES_WARN],
)
def test_criteria_warning(page, criteria, bad_html, code):
    page.set_content(f"<html><body>{bad_html}</body></html>")
    soup = BeautifulSoup(page.content(), "html5lib")
    results = list(criteria.test(page, soup))
    codes = set((r.TYPE, r.code) for r in results)
    assert ("Warning", code) in codes


@pytest.mark.parametrize(
    "criteria, bad_html, code",
    [(c, bad_html, code) for c in criteria for bad_html, code in c.EXAMPLES_ERROR],
)
def test_criteria_error(page, criteria, bad_html, code):
    page.set_content(f"<html><body>{bad_html}</body></html>")
    soup = BeautifulSoup(page.content(), "html5lib")
    results = list(criteria.test(page, soup))
    codes = set((r.TYPE, r.code) for r in results)
    assert ("Error", code) in codes
