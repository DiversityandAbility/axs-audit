from audit.ask import ask
from audit.results import AXSFailure
from audit.techniques.base import Technique


class F39(Technique):
    code = "F39"
    code_description = "Failure of Success Criterion 1.1.1 due to providing a text alternative that is not null (e.g., alt='spacer' or alt='image') for images that should be ignored by assistive technology"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/failures/F39"

    def __init__(self, criteria=None):
        self.criteria = criteria

    """
    Identify any img elements that are used for decoration, spacing or other purpose that is not part of the meaningful content in the page
    Check that the alt attribute for these elements is null.
    """

    def elements_needed(self):
        return ["img"]

    def test(self, element):
        human_answer = ask(
            element,
            "Is this image purely decorative?",
            ("Y", "Yes"),
            ("N", "No"),
        )
        if human_answer == "Y":
            alt_text = element.get_attribute("alt")
            if alt_text != "":
                yield AXSFailure(self.code, self.code_description, element)
