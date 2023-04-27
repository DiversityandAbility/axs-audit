from audit.results import AXSSkipped
from audit.techniques.base import Technique


class F3(Technique):
    code = "F3"
    code_description = "Failure of Success Criterion 1.1.1 due to using CSS to include images that convey important information"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/failures/F3"

    """
    Procedure
    Examine all images added to the content via CSS, HTML style attributes, or dynamically in script as background images.
    Check that the images do not convey important information.
    If an image does convey important information, the information is provided to assistive technologies and is also available when the CSS image is not displayed.

    If 2 and 3 are both False, then the content fails the criteria
    """

    def elements_needed(self):
        return [] #unsure how to check if included in CSS

    def test(self, element):
        # ALT! Do not know how to check if included in CSS
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
        """
        # TODO
        # if element is image
        # check if added to content via CSS, HTML style attributes, or dynamically in script as background images
        human_answer = ask(
            element,
            "Does this image convey important information to the user?",
            ("Y", "Yes"),
            ("N", "No"),
        )
        if human_answer == "Y":
            # if element's information is provided to assistive technologies + is also available when the CSS image is not displayed:
            #       yield AXSSufficient/Skipped/Whatever should be passed back on Not A Failure
            # else:
            yield AXSFailure(
                self.code,
                "CSS to include images that convey important information",
                element,
            )
        """
