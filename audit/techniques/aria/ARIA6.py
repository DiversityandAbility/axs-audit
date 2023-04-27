from audit.techniques.base import Technique
from audit.results import AXSSkipped, AXSSufficient
from audit.ask import ask


class ARIA6(Technique):
    code = "ARIA6"
    code_description = "Using aria-label to provide labels for objects"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA6"

    """
    For each element where a aria-label attribute is present.

    Examine whether the text description accurately labels the object or provides a description of its purpose or provides equivalent information.

    """

    def elements_needed(self):
        # For each element where an aria-label is present.
        return "aria-label" #?

    def test(self, element):
        aria_label = element.getAttribute("aria-label") # is this going to be in img, object, svg, audio, video from a_1_1_1?
        if aria_label is not None:
            human_answer = ask(
                element,
                f"Does the text description '{aria_label}' accurately label the object, provide a description of the objects purpose, or provides equivalent information?",
                ("Y", "Yes"),
                ("N", "No"),
            )
            if human_answer == "Y":
                yield AXSSufficient(
                    self.code,
                    self.code_description,
                    element
                )
        # yield AXSSkipped(self.code, self.code_description, element)
