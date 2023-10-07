from audit.results import Ask, Met, ResultType, TechniqueResult
from audit.techniques.base import Technique
from audit.techniques.general.G88 import G88


class H25(Technique):
    code = "H25"
    code_description = "Providing a title using the title element"
    reading = "https://www.w3.org/WAI/WCAG22/Techniques/html/H25"

    def test(self, page, context, type):
        html = page.locator("html")
        title = page.locator("css=head title")

        if not title:
            yield TechniqueResult(
                self.code,
                "There is no page title in the <head>",
                html,
                is_met=Met.NO,
                type=type,
            )
            return

        if not title.text_content().strip():
            yield TechniqueResult(
                self.code,
                "The page title is empty",
                html,
                is_met=Met.NO,
                type=type,
            )
            return

        res = list(G88().test(page, context, type))
        yield from res

        condition = Met.YES
        if type == ResultType.FAILURE:
            condition = Met.NO

        if any(r.is_met == Met.UNKNOWN for r in res):
            yield TechniqueResult(
                self.code,
                "We do not know if the title element provides a title",
                html,
                is_met=Met.UNKNOWN,
                type=type,
            )
        elif all(r.is_met == condition for r in res):
            yield TechniqueResult(
                self.code,
                "The title element provides a title",
                html,
                is_met=Met.YES,
                type=type,
            )
        else:
            yield TechniqueResult(
                self.code,
                "The title element does not provide a title",
                html,
                is_met=Met.NO,
                type=type,
            )
