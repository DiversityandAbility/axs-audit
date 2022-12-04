from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class H67(Technique):
    code = "H67"
    code_description = "Using null alt text and no title attribute on img elements for images that assistive technology should ignore"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H67"


    """ How to check:

    1. Check that title attribute is either absent or empty.
    2. Check that alt attribute is present and empty.
    
    All checks are True to be sufficient
    """

    def test(self, element):
        human_answer = ""
        while human_answer != "Y" and human_answer != "N":
            human_answer = self.ask("Is this image purely decorative? Y/N", element).upper()
        if human_answer == "Y":
            alt_text = element.getAttribute("alt")
            title_text = element.getAttribute("title")
            if (title_text == None or title_text == "") and alt_text == "":
                yield AXSSufficient(
                    self.code,
                    self.code_description,
                    element
                )
