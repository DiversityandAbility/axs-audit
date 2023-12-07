from audit.criteria.base import Criteria, Level
from audit.results import CriteriaResult, ResultType
from audit.techniques.html.H98 import H98
from audit.techniques.failures.F107 import F107


class C_1_3_5(Criteria):
    level = Level.AA
    ref = "1.3.5"
    name = "Identify Input Purpose"
    summary = """

The purpose of each input field collecting information about the user can be programmatically determined when:

    The input field serves a purpose identified in the Input Purposes for user interface components section; and
    The content is implemented using technologies with support for identifying the expected meaning for form input data.

""" # too long a summary? too tired to know what it should say

    def test(self, page, context):
        res = list(H98().test(page, context, type=ResultType.SUFFICIENT))
        res.extend(F107().test(page, context, type=ResultType.FAILURE))
        yield from res

        yield CriteriaResult(self.ref, self.summary, self.is_met(res))

    
