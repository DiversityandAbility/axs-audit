from audit.results import AXSSufficient, AXSSkipped
from audit.techniques.base import Technique

class PDF1(Technique):
    code = "PDF1"
    code_description = "Applying text alternatives to images with the Alt entry in PDF documents"
    reading = "https://www.w3.org/WAI/WCAG21/Techniques/pdf/PDF1"


    """ How to check:

    1. Verify the images have /Alt entries on an enclosing tag by one of the following:

        a. Read the PDF document with a screen reader, listening to hear that the equivalent text is read when tabbing to the non-text object (if it is tabbable) or hearing the alternative text read when reading the content line-by-line.
        b. Using a PDF editor, check that a text alternative is displayed for each image.
        c. Use a tool which is capable of showing the /Alt entry value, such as aDesigner, to open the PDF document and view the GUI summary to read the text alternatives for images.
        d. Use a tool that exposes the document through the accessibility API and verify that images have required text equivalents.
    
    1. is True to be sufficient
    """

    def test(self, element):
        yield AXSSkipped(
            self.code,
            self.code_description,
            element,
        )
