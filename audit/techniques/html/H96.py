from audit.results import AXSSkipped
from audit.techniques.base import Technique


class H96(Technique):
    code = "H96"
    code_description = "Using the track element to provide audio descriptions"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H96"

    """
    For each video element used to play a video:

    Check that the video contains a track element of kind descriptions in the language of the video.
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
        """
        # HOW TO FIND TRACK???
        track = element.get_attribute("track")  # ???
        if track:
            # ask for language from user here? how to validate input for language?? give options???
            lang = "en"  # TEMP
            # lang = ask(element, "What language is this video?")
            if (
                track.get_attribute("kind") == "descriptions"
                and track.get_attribute("srclang") == lang
            ):
                yield AXSAdvisory(self.code, self.code_description, element)
        """
