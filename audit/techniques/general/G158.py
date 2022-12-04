from audit.results import AXSSkipped
from audit.techniques.base import Technique


class G158(Technique):
    code = "G158"
    code_description = (
        "Providing an alternative for time-based media for audio-only content"
    )
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/general/G158"

    """
    1. View the audio-only content while referring to the alternative for time-based media.
    2. Check that the dialogue in the transcript matches the dialogue and information presented in the audio-only presentation.
    3. If the audio includes multiple voices, check that the transcript identifies who is speaking for all dialogue.
    4. Check that at least one of the following is true:
        a. The transcript itself can be programmatically determined from the text alternative for the audio-only content
        b. The transcript is referred to from the programmatically determined text alternative for the audio-only content
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
        # this is a horrible way to do this
        human_answer = ask(
            element,
            "Does the diaglogue in the transcript match the dialogue/information presented in the audio-only presentation?",
            ("Y", "Yes"),
            ("N", "No"),
        )
        if human_answer == "Y":
            human_answer = ask(
                element,
                "If multiple voices are speaking, does ths transcript identify who is speaking for all dialogue?",
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
