Python module per WCAG item:
    EXAMPLE_PASS
    EXAMPLE_FAIL - both HTML strings that show how to pass or fail the item
    def test() - takes in a browser client object and yields Warning or Failure objects
    Warning|Failure - essentially tuples of (WCAG_CODE, page, location)

The python modules can be used to iterate through all of the WCAG items.
    So we can auto build tests using EXAMPLE_PASS EXAMPLE_FAIL
    We can build documentation and example pages

To start the scan need a config file that provides a set of seeds:
    Seeds are tuples of (action, location, data)
        e.g. (visit "google.com")
        e.g. (type "#username" "hello")

Crawl sites using browser thing, for each page pass it thorugh all the modules.