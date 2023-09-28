from audit.criteria.base import Criteria, Level
from audit.results import Advisory, ResultType
from audit.techniques.html.H57 import H57
from audit.techniques.server.SVR5 import SVR5


class C_3_1_1(Criteria):
    level = Level.A
    ref = "3.1.1"
    name = "Language of Page"
    summary = "Make sure that the language identified in the code is the language used on the page."

    def test(self, page, context):
        html = page.locator("html")
        yield from H57().test(html, context)
        for result in SVR5().test(html, context):
            if result.TYPE == ResultType.FAILURE:
                yield Advisory.from_(result)
            else:
                yield result
