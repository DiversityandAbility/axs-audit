from audit.results import AXSSkipped
from audit.techniques.base import Technique


class G166(Technique):
    code = "G166"
    code_description = "Providing audio that describes the important video content and describing it as such"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/general/G166"

    """
    For a Web page that contains video-only content:

    Check that there is link to an audio alternative which describes the contents of the video immediately before or after the video-only content.

    If 1. is True then technique is sufficient
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
        """
        # note? video-only means no audio, just video. Almost certainly
        # needs a check to ask if the element is audio only or video only, otherwise 1_2_1 won't apply here
        human_answer = ask(
            element,
            "Is there a link to an audio alternative which describes the content of the video-only content?",
            ("Y", "Yes"),
            ("N", "No"),
        )
        if human_answer == "Y":
            yield AXSSufficient(self.code, self.code_description, element)
        """
