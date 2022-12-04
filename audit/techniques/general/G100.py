from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class G100(Technique):
    code = "G100"
    code_description = "Providing a short text alternative which is the accepted name or a descriptive name of the non-text content"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/general/G100"


    """ How to check:
    
    1. Check that short text alternative provides a descriptive name.
    2. Check that short text alternative provides a name that has previously been given to the non-text content by the author or another.
    
    1. or 2. is True to be sufficient
    """

    def test(self, element):
        # ??? can be tested without these but also can include these??
        """
        Includes:
        - ARIA6
        - ARIA10
        - G196
        - H2
        - H37
        - H53
        - H86
        - PDF1
        """
        
        human_answer = ""
        while human_answer != "Y" and human_answer != "N":
            human_answer = self.ask("Does this image provide a sensory experience? (e.g. a work of art) Y/N", element).upper()
        if human_answer == "Y":
            alt_text = element.getAttribute("alt")
            if alt_text:
                human_answer = ""
                while human_answer != "Y" and human_answer != "N":
                    human_answer = self.ask("Does the alt text '" + alt_text + "' provide a descriptive name of the work, or the name of the artwork (such as 'Mona Lisa, by Leonardo da Vinci')? Y/N", element).upper()
                if human_answer == "Y":
                    yield AXSSufficient(
                        self.code,
                        self.code_description,
                        element,
                    )
