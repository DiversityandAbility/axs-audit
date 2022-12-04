from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class H44(Technique):
    code = "H44"
    code_description = "Using label elements to associate text labels with form controls"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H44"


    """ How to check:

    For all input elements of type text, file or password, for all textarea elements, and for all select elements in the Web page:

    1. Check that there is a label element that identifies the purpose of the control before the input, textarea, or select element
    2. Check that the for attribute of the label element matches the id of the input, textarea, or select element.
    3. Check that the label element is visible.

    For all input elements of type checkbox or radio in the Web page:

    1. Check that there is a label element that identifies the purpose of the control after the input element.
    2. Check that the for attribute of the label element matches the id of the input element.
    3. Check that the label element is visible.

    1. and 2. must be True, and if the success criterion is also 3.3.2, 3. must be True
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )