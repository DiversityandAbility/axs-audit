from audit.results import Met, TechniqueResult, Ask
from audit.techniques.base import Technique


class SVR5(Technique):
    code = "SVR5"
    code_description = "Specifying the default language in the HTTP header"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/server-side-script/SVR5.html"

    def test(self, page, context, type):
        html = page.locator("html")

        header_lang = context["response"].header_value("Content-Language")
        if not header_lang:
            yield TechniqueResult(
                self.code,
                "The server did not set a 'Content-Language' header.",
                html,
                is_met=Met.NO,
                type=type,
            )
            return

        qid = f"page-language-{header_lang}-{html.page.url}"
        lang_matches = context["answers"].get(qid, None)
        if lang_matches is None:
            yield Ask(
                self.code,
                f"Does the language of this page appear to be {header_lang}?",
                html,
                type,
                qid,
                Ask.YESNO,
            )
        elif not lang_matches:
            yield TechniqueResult(
                self.code,
                "The 'Content-Language' header value does not match the observed language of the page.",
                html,
                is_met=Met.NO,
                type=type,
            )
        else:
            yield TechniqueResult(
                self.code,
                "The 'Content-Language' header value matches the observed language of the page.",
                html,
                is_met=Met.YES,
                type=type,
            )
