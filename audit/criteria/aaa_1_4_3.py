"""
The principle 1, guildeline 4 point 3 criteria ensure that the contrast
between text and the background meets a minimum level.

For instance text that is faded might be so faded as to be unreadable for some users.

Guidelines: https://www.w3.org/TR/WCAG22/#contrast-minimum
How to meet: https://www.w3.org/WAI/WCAG22/quickref/#contrast-minimum
"""


def test(page):
    # https://stackoverflow.com/questions/2579666/getelementsbytagname-equivalent-for-textnodes
    failures = page.evaluate(
        """
        () => {
            let walker = document.createTreeWalker(
                document.body,
                NodeFilter.SHOW_TEXT
            );
            let failures = [];

            let currentNode = walker.currentNode;
            while(currentNode) {
                let style = getComputedStyle(currentNode.parentElement);
                failures.push([currentNode, style.color, style.backgroundColor, currentNode.nodeValue]);
                currentNode = walker.nextNode();
            }
            return failures;
        }
    """
    )
    # print(failures)
    yield
    # Using JS find all text elements
    # use getComputedStyle()
    # check ratios


EXAMPLES_PASS = [
    "<div style='background-color: white'><p style='color: black'>This is some readable text</p></div>"
]
EXAMPLES_WARN = [
    # An image with text in it
]
EXAMPLES_ERROR = [
    (
        "<div style='background-color: #333'><p style='color: #444'>This is some unreadable text</p></div>",
        "G18",
    ),
    (
        "<div style='background-color: #333;font-size:19pt'><p style='color: #444'>This is some unreadable text</p></div>",
        "G145",
    ),
]
