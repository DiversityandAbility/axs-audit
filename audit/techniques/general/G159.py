from audit.results import AXSSkipped
from audit.techniques.base import Technique


class G159(Technique):
    code = "G159"
    code_description = (
        "Providing an alternative for time-based media for video-only content"
    )
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/general/G159"

    """
    1. View the video-only content while referring to the alternative for time-based media.
    2. Check that the information in the transcript includes the same information that is in the video-only presentation.
    3. If the video includes multiple people or characters, check that the transcript identifies which person or character is associated with each action described.
    4. Check that at least one of the following is true:
        a. The transcript itself can be programmatically determined from the text alternative for the video-only content
        b. The transcript is referred to from the programmatically determined text alternative for the video-only content
    5. If the alternate version(s) are on a separate page, check for the availability of link(s) to allow the user to get to the other versions.

    All checks are true
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
        """
        human_answer = ask(
            element,
            "Does the information in the transcript match the information presented in the video-only presentation?",
            ("Y", "Yes"),
            ("N", "No"),
        )
        if human_answer == "Y":
            human_answer = ask(
                element,
                "If multiple people or characters were in the video, does this transcript identify who is doing each action?",
                ("Y", "Yes"),
                ("N", "No"),
            )
            if human_answer == "Y":
                human_answer = ask(
                    element,
                    "If the text alternatives are on a seperate page, are there links on the current page to access the text alternatives?",
                    ("Y", "Yes"),
                    ("N", "No"),
                )
                if human_answer == "Y":
                    # TODO
                    # How to check:
                    # - The transcript itself can be programmatically determined from the text alternative for the audio-only content
                    # - The transcript is referred to from the programmatically determined text alternative for the audio-only content
                    yield AXSSufficient(
                        self.code,
                        self.code_description,
                        element
                    )
        """
