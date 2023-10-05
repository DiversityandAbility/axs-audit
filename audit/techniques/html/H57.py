from audit.results import Ask, Met, TechniqueResult
from audit.techniques.base import Technique


class H57(Technique):
    code = "H57"
    code_description = "Using the language attribute on the HTML element"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H57.html"

    def test(self, page, context, type):
        html = page.locator("html")

        lang_attr = html.get_attribute("lang")
        if not lang_attr:
            yield TechniqueResult(
                self.code,
                "The <html> element does not have a 'lang' attribute.",
                html,
                is_met=Met.NO,
                type=type,
            )
            return

        qid = f"page-language-{lang_attr}-{html.page.url}"
        lang_matches = context["answers"].get(qid, None)
        if lang_matches is None:
            yield Ask(
                self.code,
                f"Does the language of this page appear to be {lang_attr}?",
                html,
                type,
                qid,
                Ask.YESNO,
            )
        elif not lang_matches:
            yield TechniqueResult(
                self.code,
                "The 'lang' attribute of the <html> element does not match the observed language of the page.",
                html,
                is_met=Met.NO,
                type=type,
            )
        else:
            yield TechniqueResult(
                self.code,
                "The 'lang' attribute of the <html> element matches the observed language of the page.",
                html,
                is_met=Met.YES,
                type=type,
            )
