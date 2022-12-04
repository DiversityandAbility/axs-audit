from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class G92(Technique):
    code = "G92"
    code_description = "Providing long description for non-text content that serves the same purpose and presents the same information"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/general/G92"


    """ How to check:
    
    1. Remove, hide, or mask the non-text content
    2. Display the long description
    3. Check that the long description conveys the same information conveyed by the non-text content.
    
    3. is True to be sufficient
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )