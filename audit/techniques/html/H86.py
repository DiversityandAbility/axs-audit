from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class H86(Technique):
    code = "H86"
    code_description = "Providing text alternatives for emojis, emoticons, ASCII art, and leetspeak"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H86"


    """ How to check:

    1. Check to see that the content contains emojis, emoticons, ASCII art, or leetspeak.
    2. Check that each emoji has a text alternative that serves an equivalent purpose.
    3. Check that each ASCII artwork, emoticon, and / or Leetspeak either:
        a. is marked up as an image with a text alternative that serves an equivalent purpose; or
        b. has a text alternative immediately before or after.
    
    2. and 3. are True to be sufficient
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )