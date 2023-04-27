from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class H53(Technique):
    code = "H53"
    code_description = "Using the body of the object element"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H53"


    """ How to check:

    1. Check that the body of each object element contains a text alternative for the object.
    
    1. is True to be sufficient
    """

    def elements_needed(self):
        return ["object"]

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )