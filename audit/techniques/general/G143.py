from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class G143(Technique):
    code = "G143"
    code_description = "Providing a text alternative that describes the purpose of the CAPTCHA"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/general/G143"


    """ How to check:
    
    1. Remove, hide, or mask the CAPTCHA.
    2. Replace it with the text alternative.
    3. Check that the text alternative describes the purpose of the CAPTCHA.
    
    3. is True to be sufficient
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
