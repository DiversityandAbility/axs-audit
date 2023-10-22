from audit.results import Met, TechniqueResult, Ask, ResultType
from audit.techniques.base import Technique
from audit.techniques.html.H59 import H59


class G127(Technique):
    code = "G127"
    code_description = "Identifying a Web page's relationship to a larger collection of Web pages"
    reading = "https://www.w3.org/WAI/WCAG22/Techniques/general/G127"

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
        qid = f"page-title-identify-{page.url}"
        title_identifies = context["answers"].get(qid, None)
        if title_identifies is None:
            yield Ask(
                self.code,
                f"Does this title identify the page's relationship to a larger collection of Web pages? {title.text_content()}",
                html,
                type,
                qid,
                Ask.YESNO,
            )
        elif not title_identifies:
            yield TechniqueResult(
                    self.code,
                    "The title of the page does not identify it to a larger collection of web pages",
                    html,
                    is_met=Met.NO,
                    type=type,
                )
        else:
            H59Result = yield from H59().test(page, context, type=ResultType.ADVISORY)
            if H59Result.is_met == Met.NO:
                yield TechniqueResult(
                    self.code,
                    "The title of the page does not identify it to a larger collection of web pages",
                    html,
                    is_met=Met.NO,
                    type=type,
                )
            else:
                yield TechniqueResult(
                        self.code,
                        "The title of the page does identify it to a larger collection of web pages",
                        html,
                        is_met=Met.YES,
                        type=type,
                    )