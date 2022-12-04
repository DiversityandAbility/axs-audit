from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class G73(Technique):
    code = "G73"
    code_description = "Providing a long description in another location with a link to it that is immediately adjacent to the non-text content"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/general/G73"


    """ How to check:
    
    1. Check for the presence of a link immediately before or after the non-text content
    2. Check that the link is a valid link that points directly to the long description of this particular non-text content.
    3. Check that the long description conveys the same information as the non-text content
    4. Check for the availability of a link or back function to get the user back to the original location of the non-text content
    
    All 4 are True to be sufficient
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )