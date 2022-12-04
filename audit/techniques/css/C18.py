from audit.results import AXSSufficient, AXSWarning, AXSSkipped
from audit.techniques.base import Technique


class C18(Technique):
    code = "C18"
    code_description = "Using CSS margin and padding rules instead of spacer images for layout design"
    reading = "https://www.w3.org/WAI/WCAG22/Techniques/css/C18"


    def test(self, element):
        """
        "Tests - No tests available for this technique."
        WHAT, HUH
        """
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
