from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class H24(Technique):
    code = "H24"
    code_description = "Providing text alternatives for the area elements of image maps"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H24"


    """ How to check:

    For each area element in an image map:

    1. Check that the area element has an alt attribute.
    2. Check that the text alternative specified by the alt attribute serves the same purpose as the part of image map image referenced by the area element of the image map.
    
    All checks are True to be sufficient
    """

    def test(self, element):
        # ALT! Unsure how to check for images inside a <map>
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )