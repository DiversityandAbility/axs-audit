from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class H36(Technique):
    code = "H36"
    code_description = "Using alt attributes on images used as submit buttons"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H36"


    """ How to check:

    1. For all input elements that have a type attribute value of image, check for the presence of an alt attribute.
    2. Check that the value of the alt attribute describes the button's function.
    
    Both are True to be sufficient
    """

    def elements_needed(self):
        return ["input", 'type="image"']

    def test(self, element):
        # ALT! Unsure of how to check for input elements/buttons
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )