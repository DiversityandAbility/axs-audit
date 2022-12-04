from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class PDF4(Technique):
    code = "PDF4"
    code_description = "Hiding decorative images with the Artifact tag in PDF documents"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/pdf/PDF4"


    """ How to check:

    1. For an image that is purely decorative, use one of the following to verify that it is marked as an artifact:

        a. Read the PDF document with a screen reader, listening to hear that the decorative image is not announced when reading the content line-by-line.
        b. Using a PDF editor, make sure the decorative image is marked as an artifact.
        c. Reflow the document and make sure the decorative image does not appear on the page.
        d. Use a tool that is capable of showing the /Artifact entry or property list, such as aDesigner, to open the PDF document and verify that decorative images are marked as artifacts.
        e. Use a tool that exposes the document through the accessibility API and verify that the decorative image is not exposed through the API.
    
    1. is True to be sufficient
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
