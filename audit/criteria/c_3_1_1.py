from audit.criteria.base import Criteria, Level
from audit.results import CriteriaResult, ResultType
from audit.techniques.html.H57 import H57
from audit.techniques.server.SVR5 import SVR5


class C_3_1_1(Criteria):
    level = Level.A
    ref = "3.1.1"
    name = "Language of Page"
    summary = "Make sure that the language identified in the code is the language used on the page."

    def test(self, page, context):
        yield from SVR5().test(page, context, type=ResultType.ADVISORY)

        res = list(H57().test(page, context, type=ResultType.SUFFICIENT))
        yield from res

        yield CriteriaResult(self.ref, self.summary, self.is_met(res))
