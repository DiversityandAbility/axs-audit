from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class G196(Technique):
    code = "G196"
    code_description = "Using a text alternative on one item within a group of images that describes all items in the group"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/general/G196"


    """ How to check:
    
    1. Check that one item in the group includes a text alternative that serves the equivalent purpose for the entire group.
    2. Check that the other items in the group are marked in a way that can be ignored by assistive technologies.
    3. Check that the items marked in a way that can be ignored by assistive technologies are adjacent to the item that contains the text alternative for the group.
    
    All checks are True to be sufficient
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )