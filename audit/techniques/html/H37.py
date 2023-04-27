from audit.ask import ask
from audit.results import AXSSufficient
from audit.techniques.base import Technique


class H37(Technique):
    code = "H37"
    code_description = "Using alt attributes on img elements"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/html/H37"

    """
    PROCEDURE
    1. Examine each img element in the content.
    2. Check that each img element which conveys meaning contains an alt attribute.
    3. If the image contains words that are important to understanding the content, the words are included in the text alternative.

    #2 and #3 are True for this to be sufficient
    """

    def elements_needed(self):
        return ["img"]

    def test(self, element):
        # human please check, does this image need alt text
        # if yes:
        #   does it have alt text:
        #       if yes:
        #           human please check, is the alt text good
        #           if yes:
        #               yield AXSSufficient
        #       if no:
        #           ----
        # if no:
        #   ----

        human_answer = ask(
            element,
            "Does this image need alt text? (e.g not a decorative image)",
            ("Y", "Yes"),
            ("N", "No"),
        )
        if human_answer == "Y":
            alt_text = element.get_attribute("alt")
            if alt_text is not None:
                human_answer = ask(
                    element,
                    f"Does the alt text '{alt_text}' accurately describe the image? (If there are words contained in the image that are important to understanding the context, are they included in the alt text?)",
                    ("Y", "Yes"),
                    ("N", "No"),
                )
                if human_answer == "Y":
                    yield AXSSufficient(
                        self.code,
                        self.code_description,
                        element,
                    )
