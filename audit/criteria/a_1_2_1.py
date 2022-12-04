"""
The principle 1, guideline 2, point 1 criteria ensure that prerecorded
audio-only and video-only content always has an alternative where needed.
"""
from audit.ask import ask
from audit.criteria import base
from audit.techniques.general.G158 import G158
from audit.techniques.general.G159 import G159
from audit.techniques.general.G166 import G166
from audit.techniques.html.H96 import H96
from audit.techniques.failures.F30 import F30
from audit.techniques.failures.F67 import F67


class A1_2_1(base.Criteria):
    name = "1_2_1"
    level = "A"
    summary = "Alternatives for time based audio/video media"
    understanding = "https://www.w3.org/WAI/WCAG21/Understanding/audio-only-and-video-only-prerecorded.html"

    SUFFICIENT = {
        "A": G158(),
        "B": G159() | G166(),
    }

    ADVISORY = H96()

    FAILURE = F30() + F67()

    # tests are for audio only and video only
    # for F67, G158 and G159, if there is no long description, yield nothing
    #

    def test_sufficient(self, element):
        scenario = ask(element, "Which scenario?", ("A", "A"), ("B", "B"))

        techniques = self.SUFFICIENT[scenario]
        yield techniques.resolve(element)

    def find_elements(self, page):
        tags = ["audio", "video"]
        for t in tags:
            matches = page.locator(f"css={t}")
            for idx in range(matches.count()):
                yield matches.nth(idx)
