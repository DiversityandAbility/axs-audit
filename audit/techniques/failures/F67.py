from audit.results import AXSSkipped
from audit.techniques.base import Technique


class F67(Technique):
    code = "F67"
    code_description = "Failure of Success Criterion 1.1.1 and 1.2.1 due to providing long descriptions for non-text content that does not serve the same purpose or does not present the same information"
    reading = "https://www.w3.org/WAI/WCAG22/Techniques/failures/F67"

    """
    For all non-text content that requires a long description

    Check that the long description serves the same purpose or presents the same information as the non-text content.
    """

    def elements_needed(self):
        #TODO: Figure out what elements are non-text
        return []

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
        """
        # unsure about "If there is no long description, answer N" as *technically* this technique doesn't cover that
        # G158/G159 wouldn't pass if there wasn't a long description, so 1_2_1 would fail on nothing being sufficient, not on there being a failure
        human_answer = ask(
            element,
            "Does this element require a long description?",
            ("Y", "Yes"),
            ("N", "No"),
        )
        if human_answer == "Y":
            human_answer = ask(
                element,
                "Is the long description for this element serving the same purpose/presenting the same information as the non-text content?",
                ("Y", "Yes"),
                ("N", "No"),
            )
            if human_answer == "N":
                yield AXSFailure(
                    self.code,
                    "Providing long descriptions for non-text content that does not serve the same purpose or does not present the same information",
                    element,
                )
        """
