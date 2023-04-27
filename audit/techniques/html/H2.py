from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class H2(Technique):
    code = "H2"
    code_description = "Combining adjacent image and text links for the same resource"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H2"


    """ How to check:

    For each a applying this technique:
    
    1. Check that every img element contained within the a element has a null value set for its alt attribute.
    2. Check that the a element contains an img element that has either a null alt attribute value or a value that supplements the link text and describes the image
    
    All checks are True to be sufficient
    """

    def elements_needed(self):
        return ["a"]
        # how to return images inside <a>?

    def test(self, element):
        # ALT! Unsure how to check for images inside <a>
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )