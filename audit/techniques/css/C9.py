from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique


class C9(Technique):
    code = "C9"
    code_description = "Using CSS to include decorative images"
    reading = "https://www.w3.org/WAI/WCAG22/Techniques/css/C9"

    """ HOW TO CHECK
    Check for the presence of decorative images
    Check that they are included with CSS
    """

    def elements_needed(self):
        #TODO: understand what C9 actually means
        return []
    
    def test(self, element):
        # ALT! Do not know how to check if included in CSS
        # Human 1, Computer 2? Human 1+2?
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
