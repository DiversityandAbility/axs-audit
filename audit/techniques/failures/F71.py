from audit.results import AXSFailure, AXSSkipped
from audit.techniques.base import Technique


class F71(Technique):
    code = "F71"
    code_description = "Failure of Success Criterion 1.1.1 due to using text look-alikes to represent text without providing a text alternative"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/failures/F71"

    """ How to test:
    1. Check the characters or character entities used to represent text.
    2. If the characters used do not match the appropriate characters for the displayed glyphs in the human language of the content, then look-alike glyphs are being used.
    (3.? If look-alike glyphs are used, and there is not a text alternative for any range of text that uses look-alike glyphs, then the content does not meet the Success Criterion.)
    """
    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
