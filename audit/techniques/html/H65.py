from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class H65(Technique):
    code = "H65"
    code_description = "Using the title attribute to identify form controls when the label element cannot be used"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H65"


    """ How to check:

    1. Check that the control has a title attribute
    2. Check that the purpose of the form control is clear to users who can see the control.
    3. Check that the title attribute identifies the purpose of the control and that it matches the apparent visual purpose.
    
    All checks are True to be sufficient
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )