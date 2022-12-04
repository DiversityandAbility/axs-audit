from audit.results import AXSFailure, AXSSkipped
from audit.techniques.base import Technique


class F65(Technique):
    code = "F65"
    code_description = "Failure of Success Criterion 1.1.1 due to omitting the alt attribute or text alternative on img elements, area elements, and input elements of type 'image'"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/failures/F65"

    def __init__(self, criteria=None):
        self.criteria = criteria

    """
    Identify img, area and input elements of type image. For each of these elements:

    Check if the alt attribute is present.
    Check if aria-labelledby attribute is present AND references one or more id elements in the page AND check if aria-labelledby is accessibility supported.
    Check if the aria-label attribute is present AND check if aria-label is accessibility supported.
    Check if the title attribute is present AND check if title is accessibility supported.
    """
    def test(self, element):
        # TODO a lot of things depend on if an image is descriptive (F38, F39)
        # maybe change how that might work?
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
        """
        yield AXSFailure(
            self.code,
            "Omitting the alt attribute or text alternative on img elements, area elements, and input elements of type 'image'",
            element,
        )
        """
