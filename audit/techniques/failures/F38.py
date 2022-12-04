from audit.ask import ask
from audit.results import AXSFailure
from audit.techniques.base import Technique


class F38(Technique):
    code = "F38"
    code_description = "Failure of Success Criterion 1.1.1 due to not marking up decorative images in HTML in a way that allows assistive technology to ignore them"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/failures/F38"

    """
    For any img element that is used for purely decorative content:

    Check whether the element has no role attribute or has a role attribute value that is not presentation.
    Check whether the element has no alt attribute or has an alt attribute with a value that is not null.

    1 AND 2 must be true for this to fail
    """

    def test(self, element):
        human_answer = ask(
            element,
            "Is this image purely decorative?",
            ("Y", "Yes"),
            ("N", "No"),
        )
        if human_answer == "Y":
            role = element.get_attribute("role")
            alt = element.get_attribute("alt")
            if (role is None or role != "presentation") and (alt is None or alt != ""):
                yield AXSFailure(self.code, self.code_description, element)
