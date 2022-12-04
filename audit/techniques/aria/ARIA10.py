from audit.techniques.base import Technique
from audit.results import AXSSkipped


class ARIA10(Technique):
    code = "ARIA10"
    code_description = (
        "Using aria-labelledby to provide a text alternative for non-text content"
    )
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA10"

    """
    Procedure
    Examine each element where the aria-labelledby attribute is present and the element does not support the alt attribute.
    Check whether the value of the aria-labelledby attribute is the id of an element on the web page.
    Determine that the text of the element identified by the aria-labelledby attribute accurately labels the element, provides a description of its purpose, or provides equivalent information.
    """

    def test(self, element):
        # no clue how to check 1. ("examine each element" - does that mean examine page?)
        yield AXSSkipped(self.code, self.code_description, element)
