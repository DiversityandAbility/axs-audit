from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class H30(Technique):
    code = "H30"
    code_description = "Providing link text that describes the purpose of a link for anchor elements"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H30"


    """ How to check:

    For each link in the content that uses this technique:

    1. Check that text or a text alternative for non-text content is included in the a element.
    2. If an img element is the only content of the a element, check that its text alternative describes the purpose of the link.
    3. If the a element contains one or more img element(s) and the text alternative of the img element(s) is empty, check that the text of the link describes the purpose of the link.
    4. If the a element only contains text, check that the text describes the purpose of the link.
    
    All checks are True to be sufficient
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )