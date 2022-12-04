from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class H35(Technique):
    code = "H35"
    code_description = "Providing text alternatives on applet elements"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H35"


    """ How to check:

    1. View the source code of the applet element
    2. Check that the applet element contains an alt attribute with a text alternative for the applet
    3. Check that the applet element contains a text alternative for the applet in the body of the applet element
    
    2. and 3. are True to be sufficient
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )