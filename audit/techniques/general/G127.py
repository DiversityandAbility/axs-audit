from audit.results import Met, TechniqueResult, Ask
from audit.techniques.base import Technique


class G127(Technique):
    code = "G127"
    code_description = "Identifying a Web page's relationship to a larger collection of Web pages"
    reading = "https://www.w3.org/WAI/WCAG22/Techniques/general/G127"

    # TODO
    # Add in second procedure for G127 (uses rel) which I think is needed for 2.4.8, but not for 2.4.2
    # What to do if advisory version is not relevant to a web page?

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
            yield TechniqueResult(
                    self.code,
                    "The title of the page does identify it to a larger collection of web pages",
                    html,
                    is_met=Met.YES,
                    type=type,
                )