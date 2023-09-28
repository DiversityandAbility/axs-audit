from audit.results import Failure, Ask, Sufficient
from audit.techniques.base import Technique


class H57(Technique):
    code = "H57"
    code_description = "Using the language attribute on the HTML element"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H57.html"

    def test(self, element, context):
        lang_attr = element.get_attribute("lang")
        if not lang_attr:
            yield Failure(
                self.code,
                "The <html> element does not have a 'lang' attribute.",
                element,
            )
            return
        qid = f"page-language-{lang_attr}-{element.page.url}"
        lang_matches = context["answers"].get(qid, None)
        if lang_matches is None:
            yield Ask(
                self.code,
                f"Does the language of this page appear to be {lang_attr}?",
                element,
                qid,
                Ask.YESNO,
            )
        elif not lang_matches:
            yield Failure(
                self.code,
                "The 'lang' attribute of the <html> element does not match the observed language of the page.",
                element,
            )
        else:
            yield Sufficient(
                self.code,
                "The 'lang' attribute of the <html> element matches the observed language of the page.",
                element,
            )
