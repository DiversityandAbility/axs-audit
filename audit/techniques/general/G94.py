from audit.techniques.aria.ARIA10 import ARIA10
from audit.techniques.aria.ARIA6 import ARIA6
from audit.techniques.base import Technique
from audit.techniques.general.G196 import G196
from audit.techniques.html.H2 import H2
from audit.techniques.html.H37 import H37
from audit.techniques.html.H53 import H53
from audit.techniques.html.H86 import H86
from audit.techniques.pdf.PDF1 import PDF1


class G94(Technique):
    code = "G94"
    code_description = "Providing short text alternative for non-text content that serves the same purpose and presents the same information as the non-text content"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/general/G94"

    """ How to check:

    1. Remove, hide, or mask the non-text content
    2. Replace it with the text alternative
    3. Check that nothing is lost (the purpose of the non-text content is met by the text alternative)
    4. If the non-text content contains words that are important to understanding the content, the words are included in the text alternative
    
    3. is True. If 4. condition is True, then also check 4. is True.
    """

    def resolve(self, element):
        techniques = ARIA6() & ARIA10() & G196() & H2() & H37() & H53() & H86() & PDF1()
        return techniques.resolve(element)
