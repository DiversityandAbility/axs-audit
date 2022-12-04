from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class G144(Technique):
    code = "G144"
    code_description = "Ensuring that the Web Page contains another CAPTCHA serving the same purpose using a different modality"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/general/G144"


    """ How to check:
    
    1. Check that the Web page contains another CAPTCHA for the same purpose but using a different modality.
    
    1. is True to be sufficient
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
