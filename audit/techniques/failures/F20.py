from audit.ask import ask
from audit.results import AXSFailure
from audit.techniques.base import Technique


class F20(Technique):
    code = "F20"
    code_description = "Failure of Success Criterion 1.1.1 and 4.1.2 due to not updating text alternatives when changes to non-text content occur"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/failures/F20"

    """
    Check each text alternative to see if it is describing content other than the currently-displayed non-text content.
    """

    def test(self, element):
        alt_text = element.get_attribute("alt")
        if alt_text:
            human_answer = ask(
                element,
                f"Is the element's alt text '{alt_text}' describing content other than the currently displayed content?",
                ("Y", "Yes"),
                ("N", "No"),
            )
            if human_answer == "Y":
                yield AXSFailure(
                    self.code,
                    self.code_description,
                    element,
                )
