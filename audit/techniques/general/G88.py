from audit.results import Ask, Met, TechniqueResult
from audit.techniques.base import Technique


class G88(Technique):
    code = "G88"
    code_description = "Providing descriptive titles for Web pages"
    reading = "https://www.w3.org/WAI/WCAG22/Techniques/general/G88"

    def test(self, page, context, type):
        html = page.locator("html")
        title = page.locator("title")

        if not title:
            yield TechniqueResult(
                self.code,
                "There is no page title",
                html,
                is_met=Met.NO,
                type=type,
            )
            return

        qid = f"page-title-relevant-{page.url}"
        title_relevant = context["answers"].get(qid, None)
        if title_relevant is None:
            yield Ask(
                self.code,
                f"Is this title relevant to this webpage? {title.text_content()}",
                html,
                type,
                qid,
                Ask.YESNO,
            )
        elif not title_relevant:
            yield TechniqueResult(
                self.code,
                "The title of the page is not relevant",
                html,
                is_met=Met.NO,
                type=type,
            )
        else:
            qid = f"page-title-identify-{page.url}"
            can_identify = context["answers"].get(qid, None)
            if can_identify is None:
                yield Ask(
                    self.code,
                    f"Does this title identify this webpage? {title.text_content()}",
                    html,
                    type,
                    qid,
                    Ask.YESNO,
                )
            elif not can_identify:
                yield TechniqueResult(
                    self.code,
                    "The title of the page does not identify it",
                    html,
                    is_met=Met.NO,
                    type=type,
                )
            else:
                yield TechniqueResult(
                    self.code,
                    "The title of the page has a descriptive title",
                    html,
                    is_met=Met.YES,
                    type=type,
                )
