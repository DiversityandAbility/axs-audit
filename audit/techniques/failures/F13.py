from audit.ask import ask
from audit.results import AXSFailure
from audit.techniques.base import Technique


class F13(Technique):
    code = "F13"
    code_description = "Failure of Success Criterion 1.1.1 and 1.4.1 due to having a text alternative that does not include information that is conveyed by color differences in the image"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/failures/F13"

    """
    For all images in the content that convey information by way of color differences:

    Check that the information conveyed by color differences is not included in the text alternative for the image.
    """

    def elements_needed(self):
        return ["img"] #unsure if this only refers to image tags or if there's some secret
        # other image im unaware of

    def test(self, element):
        alt_text = element.get_attribute("alt")
        if alt_text:
            human_answer = ask(
                element,
                "Does the image contain content that conveys information via colour differences?",
                ("Y", "Yes"),
                ("N", "No"),
            )
            if human_answer == "Y":
                human_answer = ask(
                    element,
                    f"Does the element's alt text '{alt_text}' include this colour-based information?",
                    ("Y", "Yes"),
                    ("N", "No"),
                )
                if human_answer == "N":
                    yield AXSFailure(
                        self.code,
                        self.code_description,
                        element,
                    )
