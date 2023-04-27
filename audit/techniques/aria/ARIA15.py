from audit.criteria import base

from audit.techniques import Technique
from results import AXSSufficient, AXSWarning, AXSSkipped


class ARIA15(Technique):
    code = "ARIA15"
    code_description = "Using aria-describedby to provide descriptions of images"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA15"
    

    """
    Procedure
    Examine each image element where a aria-describedby attribute is present.
    Examine whether the aria-describedby attribute programatically associates an element with its text description, via the id attribute on the element where the text to be used as the description is found.
    Examine whether the combined text equivalent and associated text description accurately describe or provide the equivalent purpose to the object.
    """

    def elements_needed(self):
        return ["img", "AND", "aria-describedby"]

    def test(self, element):
        # TODO
        # 1 and 2 can be programmatically determined?
        # 3 needs to ask a human
        yield AXSSkipped(
            self.code,
            self.code_description,
            element
        )