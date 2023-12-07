from audit.results import Ask, Met, TechniqueResult
from audit.techniques.base import Technique


class H98(Technique):
    code = "H98"
    code_description = "Using HTML 5.2 autocomplete attributes"
    reading = "https://www.w3.org/WAI/WCAG22/Techniques/html/H98"

    def test(self, page, context, type):
        # If input, select or textarea has an autocomplete, its gotta be a reasonable one


        """ 
        if input, select or textarea:
            is there an autocomplete?
                yes:
                    # So there's some auto checks that can be done here to see if it's definitely wrong
                    # e.g. element doesn't belong to text, but a autocomplete using text is used
                    # Or we just ask the user "hey is the autocomplete correct?"
                    does the autocomplete match the value of the form field?
                        yes:
                            does the autocomplete match the label of the form field?
                                yes:
                                    SUCCESS
                                no:
                                    recommend to fix the label
                        no:
                            recommend to change the autocomplete
                no:
                    should there be an autocomplete?
                        yes:
                            recommend to add an autocomplete here (advisory?)
                        no:
                            no action
        """

        html = page.locator("html")
        yield TechniqueResult(
                self.code,
                "H98 HAS NOT BEEN IMPLEMENTED YET",
                html,
                is_met=Met.NO,
                type=type,
            )


