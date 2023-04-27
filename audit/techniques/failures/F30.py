from audit.ask import ask
from audit.results import AXSFailure
from audit.techniques.base import Technique


class F30(Technique):
    code = "F30"
    code_description = "Failure of Success Criterion 1.1.1 and 1.2.1 due to using text alternatives that are not alternatives (e.g., filenames or placeholder text)"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/failures/F30"

    """
    Check each text alternative to see if it is not actually a text alternative for the non-text content.
    """

    def elements_needed(self):
        return ["alt"]

    def test(self, element):
        alt_text = element.get_attribute("alt")
        if alt_text:
            human_answer = ask(
                element,
                f"The alt text of this element is: '{alt_text}'. Is this alt text a placeholder? E.g. 'picture', '0001', 'chart.jpg'.",
                ("Y", "Yes"),
                ("N", "No"),
            )
            if human_answer == "Y":
                # not good
                yield AXSFailure(
                    self.code,
                    "Using text alternatives that are not alternatives (e.g., filenames or placeholder text)",
                    element,
                )
