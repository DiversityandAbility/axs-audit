from audit.results import AXSFailure, AXSSkipped
from audit.techniques.base import Technique


class F72(Technique):
    code = "F72"
    code_description = "Failure of Success Criterion 1.1.1 due to using ASCII art without providing a text alternative"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/failures/F72"


    """How to test

    1. Access a page with ASCII art.
    2. For each instance of ASCII art, check that it has a text alternative.

    if 2. is false, this fails
    
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
