from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class G74(Technique):
    code = "G74"
    code_description = "Providing a long description in text near the non-text content, with a reference to the location of the long description in the short description"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/general/G74"


    """ How to check:
    
    1. Check that the short text alternative includes the location of the long description
    2. Check that the long description is near the non-text content both visually and in the linear reading order
    3. Check that the long description conveys the same information as the non-text content
    
    All 3 are True to be sufficient
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )