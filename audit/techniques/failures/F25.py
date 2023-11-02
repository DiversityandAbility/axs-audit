from audit.results import Ask, Met, ResultType, TechniqueResult
from audit.techniques.base import Technique
from audit.techniques.general.G88 import G88


class F25(Technique):
    code = "F25"
    code_description = "Failure of Success Criterion 2.4.2 due to the title of a Web page not identifying the contents"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/failures/F25"

    def test(self, page, context, type):
        html = page.locator("html")
        title = page.locator("css=head title")

        if not title:
            yield TechniqueResult(
                self.code,
                "There is no page title",
                html,
                is_met=Met.YES,
                type=type,
            )
            return

        qid = f"page-title-relevant-{page.url}"
        title_relevant = context["answers"].get(qid, None)
        # TODO in future:
        # G88 is very similar to F25 in terms of what they ask. May need to change how F25 works
        # to be smarter
        if title_relevant is None:
            yield Ask(
                self.code,
                f"Does this title identify the contents or purpose of this webpage? {title.text_content()}",
                html,
                type,
                qid,
                Ask.YESNO,
            )
        elif not title_relevant:
            yield TechniqueResult(
                self.code,
                "The title does not identify the contents or purpose of this webpage.",
                html,
                is_met=Met.YES,
                type=type,
            )
        yield TechniqueResult(
                self.code,
                "The title does identify the contents or purpose of this webpage.",
                html,
                is_met=Met.NO,
                type=type,
            )


