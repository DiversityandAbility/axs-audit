from audit.results import AXSFailure, AXSSkipped
from audit.techniques.base import Technique


class G68(Technique):
    code = "G68"
    code_description = "Providing a short text alternative that describes the purpose of live audio-only and live video-only content"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/general/G68"

    """
    How to test:

    1. Remove, hide, or mask the non-text content.
    2. Display the short text alternative(s).
    3. Check that the purpose of the non-text content is clear, even if content is lost.

    Sufficient if 3. is true
    """

    def test(self, element):
        """
        Includes:
        - ARIA6
        - ARIA10
        - G196
        - H2
        - H37
        - H53
        - H86
        - PDF1
        """
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
