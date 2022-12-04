from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class G82(Technique):
    code = "G82"
    code_description = "Providing a text alternative that identifies the purpose of the non-text content"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/general/G82"


    """ How to check:
    
    1. Remove, hide, or mask the non-text content
    2. Replace it with the text alternative
    3. Check that the purpose of the non-text content is clear - even if function is lost.
    
    3. is True to be sufficient
    """

    def test(self, element):
        # ALT! Do not know how to remove, hide or mask the non-text content
        """
        Includes:

        - ARIA6
        - ARIA9
        - H24
        - H30
        - H36
        - H44
        - H65
        
        """
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
