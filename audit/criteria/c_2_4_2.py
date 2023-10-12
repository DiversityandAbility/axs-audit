from audit.criteria.base import Criteria, Level
from audit.results import CriteriaResult, ResultType
from audit.techniques.general.G88 import G88
from audit.techniques.html.H25 import H25
from audit.techniques.general.G127 import G127


class C_2_4_2(Criteria):
    level = Level.A
    ref = "2.4.2"
    name = "Page Titled"
    summary = "Web pages have titles that describe topic or purpose."

    def test(self, page, context):
        yield from G127().test(page, context, type=ResultType.ADVISORY)

        res = list(G88().test(page, context, type=ResultType.SUFFICIENT))
        res.extend(H25().test(page, context, type=ResultType.SUFFICIENT))
        yield from res

        yield CriteriaResult(self.ref, self.summary, self.is_met(res))
