from audit.techniques.base import Technique
from audit.results import AXSSkipped


class ARIA6(Technique):
    code = "ARIA6"
    code_description = "Using aria-label to provide labels for objects"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA6"

    """
    For each element where a aria-label attribute is present.

    Examine whether the text description accurately labels the object or provides a description of its purpose or provides equivalent information.

    """

    def test(self, element):
        yield AXSSkipped(self.code, self.code_description, element)
        """
        # TODO
        # needs a check for if it has an aria-label
        # if aria-label, do the following ask-code, otherwise return AXSResult (no aria-label)
        label = element.get_attribute("aria-label")
        if label:
            human_answer = ask(
                element,
                f"Does the text description '{label}' accurately label the object, provide a description of the objects purpose, or provides equivalent information?",
                ("Y", "Yes"),
                ("N", "No"),
            )
            if human_answer == "Y":
                yield AXSSufficient(
                    self.code,
                    self.code_description,
                    element,
                )
        """
