from audit.results import Ask, Met, TechniqueResult
from audit.techniques.base import Technique


class F107(Technique):
    code = "F107"
    code_description = "Using HTML 5.2 autocomplete attributes"
    reading = "https://www.w3.org/WAI/WCAG22/Techniques/html/H98"


    """

    For each form field which collects information about the user of the form:

    Check that the form field has an autocomplete attribute and value pair that does not match the purpose of the input.
    Check that the input purpose is not communicated programmatically through any other method.


    I understand the first part (should be half checked in H98)
    2nd part???
        ok ihave genuinely been looking up the 2nd part for about 40 minutes now
        i do not think this is anything we can test for and this is a case of wcag going
        "oh well if you think up a solution to still making plugins work even if the autocomplete is wrong then you're fine"
        but won't elaborate on any examples

    """

    def test(self, page, context, type):
        html = page.locator("html")
        yield TechniqueResult(
                self.code,
                "F107 HAS NOT BEEN IMPLEMENTED YET",
                html,
                is_met=Met.NO,
                type=type,
            )