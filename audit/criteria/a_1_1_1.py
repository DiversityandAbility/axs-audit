"""
The principle 1, guideline 1, point 1 criteria ensure that non-text content
always has a text alternative where needed.

The most obvious examples of this are images that need an accompanying written
description in order to be understood by users not able to perceive the image
in its original format.

Guidelines: https://www.w3.org/TR/WCAG22/#non-text-content
How to meet: https://www.w3.org/WAI/WCAG22/quickref/#non-text-content
"""
from audit.ask import ask
from audit.criteria import base
from audit.techniques.aria.ARIA10 import ARIA10
from audit.techniques.aria.ARIA15 import ARIA15
from audit.techniques.aria.ARIA6 import ARIA6
from audit.techniques.css.C18 import C18
from audit.techniques.css.C9 import C9
from audit.techniques.failures.F30 import F30
from audit.techniques.failures.F38 import F38
from audit.techniques.failures.F39 import F39
from audit.techniques.failures.F65 import F65
from audit.techniques.failures.F67 import F67
from audit.techniques.failures.F71 import F71
from audit.techniques.failures.F72 import F72
from audit.techniques.general.G100 import G100
from audit.techniques.general.G143 import G143
from audit.techniques.general.G144 import G144
from audit.techniques.general.G196 import G196
from audit.techniques.general.G68 import G68
from audit.techniques.general.G73 import G73
from audit.techniques.general.G74 import G74
from audit.techniques.general.G82 import G82
from audit.techniques.general.G92 import G92
from audit.techniques.general.G94 import G94
from audit.techniques.general.G95 import G95
from audit.techniques.failures.F13 import F13
from audit.techniques.failures.F20 import F20
from audit.techniques.failures.F3 import F3
from audit.techniques.html.H2 import H2
from audit.techniques.html.H35 import H35
from audit.techniques.html.H37 import H37
from audit.techniques.html.H46 import H46
from audit.techniques.html.H53 import H53
from audit.techniques.html.H67 import H67
from audit.techniques.html.H86 import H86
from audit.techniques.pdf.PDF1 import PDF1
from audit.techniques.pdf.PDF4 import PDF4


class A1_1_1(base.Criteria):
    name = "1_1_1"
    level = "A"
    summary = "Text alternatives for non-text content"
    understanding = "https://www.w3.org/WAI/WCAG22/Understanding/non-text-content"

    B_SHORT = (
        ARIA6() | ARIA10() | G196() | H2() | H35() | H37() | H53() | H86() | PDF1()
    )
    B_LONG = ARIA15() | G73() | G74() | G92() | H53()

    SUFFICIENT = {
        "A": G94(),
        "B": G95(),
        "C": G82(),
        "D": G94() | G68() | G100(),  # TODO: Replace G94 with official list
        "E": G143() & G144(),
        "F": C9() | H67() | PDF4(),
    }
    ADVISORY = H46() & C18()
    FAILURE = (
        F3() & F13() & F20() & F30() & F38() & F39() & F65() & F67() & F71() & F72()
    )

    def test_sufficient(self, element):
        scenario = ask(
            element,
            "Which scenario?",
            ("A", "Scenario A"),
            ("B", "Scenario B"),
            ("C", "Scenario C"),
            ("D", "Scenario D"),
            ("E", "Scenario E"),
            ("F", "Scenario F"),
        )
        techniques = self.SUFFICIENT[scenario]
        yield techniques.resolve(element)

    def find_elements(self, page):
        tags = ["img", "object", "svg", "audio", "video"]
        for t in tags:
            matches = page.locator(f"css={t}")
            for idx in range(matches.count()):
                el = matches.nth(idx)
                if el.is_visible():
                    yield el
