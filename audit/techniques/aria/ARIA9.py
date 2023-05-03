from audit.techniques.base import Technique
from audit.results import AXSSkipped


class ARIA9(Technique):
    code = "ARIA9"
    code_description = (
        "Using aria-labelledby to concatenate a label from several text nodes"
    )
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA9"

    """
    Procedure
    For inputs that use aria-labelledby:

    Check that ids referenced in aria-labelledby are unique and match the ids of the text nodes that together provide the label
    Check that the concatenated content of elements referenced by aria-labelledby is descriptive for the purpose or function of the element labeled
    """

    def test(self, element):
        # TODO
        # Ashley does not understand how to test for ARIA9!
        # Check if IDs are unique --> if not, raise warning? sufficient but with is_failure = True?
        # Then ask human if "aria-labelledby is descriptive for the purpose or function of the element labeled"
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
        """
        human_answer = ""
        while human_answer != "Y" and human_answer != "N":
            human_answer = ask(
                "Is the concatenated aria-labelledby descriptive for the purpose or function of the element labeled? Y/N",
                element,
            ).upper()
        if human_answer == "Y":
            yield AXSSufficient(
                self.code,
                self.code_description,
                element,
            )
        """
