from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class G95(Technique):
    code = "G95"
    code_description = "Providing short text alternatives that provide a brief description of the non-text content"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/general/G95"


    """ How to check:
    
    1. Check for the presence of a short text alternative that provides a brief description of the non-text content.
    
    1. is True to be sufficient
    """

    def test(self, element):
        """
        Includes:
        - ARIA6
        - ARIA10
        - G196
        - H2
        - H37
        - H53
        - H86
        - PDF1

        AND

        - ARIA15
        - G73
        - G74
        - G92
        - H53
        """
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
