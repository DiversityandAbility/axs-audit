from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class H45(Technique):
    code = "H45"
    code_description = "Using longdesc"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H45"


    """ How to check:

    1. Check that the img element has a longdesc attribute.
    2. Check that the value of the longdesc attribute is a valid URI of an existing resource.
    3. Check that the content at the target of that URI contains a long description describing the original non-text content associated with it.
    
    All are True to be sufficient
    """

    def elements_needed(self):
        return ["img"]

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )