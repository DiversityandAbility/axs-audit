from audit.results import Failure, Ask, Sufficient
from audit.techniques.base import Technique


class SVR5(Technique):
    code = "SVR5"
    code_description = "Specifying the default language in the HTTP header"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/server-side-script/SVR5.html"

    def test(self, element, context):
        header_lang = context["response"].header_value("Content-Language")
        if not header_lang:
            yield Failure(
                self.code,
                "The server did not set a 'Content-Language' header.",
                element,
            )
            return
        qid = f"page-language-{header_lang}-{element.page.url}"
        lang_matches = context["answers"].get(qid, None)
        if lang_matches is None:
            yield Ask(
                self.code,
                f"Does the language of this page appear to be {header_lang}?",
                element,
                qid,
                Ask.YESNO,
            )
        elif not lang_matches:
            yield Failure(
                self.code,
                "The 'Content-Language' header value does not match the observed language of the page.",
                element,
            )
        else:
            yield Sufficient(
                self.code,
                "The 'Content-Language' header value matches the observed language of the page.",
                element,
            )
