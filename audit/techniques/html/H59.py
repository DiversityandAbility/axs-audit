from audit.results import Ask, Met, TechniqueResult
from audit.techniques.base import Technique


class H59(Technique):
    code = "H59"
    code_description = "Using the link element and navigation tools"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H59.html"

    def test(self, page, context, type):
        # Check all link elements pertaining to navigation occur in the head
            # Find all links
            # Which ones pertain to navigation?
            # If user says any links outside of head pertain to navigation, fail
        # For each link in the head section of the document which pertains to navigation check that it has
            # A rel attribute containing the link type
            # A valid href attribute to locate the appropriate resource

        # If all are true, then H59 is met
        html = page.locator("html")
        yield TechniqueResult(
                self.code,
                "H59 HAS NOT BEEN IMPLEMENTED YET",
                html,
                is_met=Met.NO,
                type=type,
            )