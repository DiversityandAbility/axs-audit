from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class H46(Technique):
    # fun fact - This technique is not referenced from any Understanding document.
    code = "H46"
    code_description = "Using noembed with embed"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H46"


    """ How to check:

    1. Check if embed element has a child noembed element
    2. Check if embed element has a noembed element that immediately follows it.
    
    1. or 2. is True
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
