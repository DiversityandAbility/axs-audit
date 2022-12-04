from collections import defaultdict
import hashlib


_ANSWERS = defaultdict(dict)


def hash_element(element):
    html = element.evaluate("node => node.outerHTML")
    h = hashlib.sha256()
    h.update(html.encode("utf8"))
    return h.hexdigest()


def get_answer(element, question):
    element = hash_element(element)
    return _ANSWERS[element].get(question)


def set_answer(element, question, answer):
    element = hash_element(element)
    _ANSWERS[element][question] = answer


def ask(element, question, *answers):
    answer = get_answer(element, question)
    if answer:
        return answer
    element.highlight()
    element.scroll_into_view_if_needed()
    buttons = "".join(
        f"<button name='answer' value='{a[0]}'>{a[1]}</button>" for a in answers
    )
    answer = element.page.evaluate(
        f"""
        () => {{
            let div = document.createElement("div");
            div.id = "axs-audit-ask-container";
            div.classList.add(localStorage.getItem("axs-audit-ask-position") || "bottom");
            div.innerHTML = "<div class='wrapper'><div class='question'><p>{question}</p><form>{buttons}</form></div><div class='position-buttons'><button class='top'>&#8593; Top &#8593;</button><button class='bottom'>&#8595; Bottom &#8595;</button></div></div>";
            document.querySelector("body").appendChild(div);
            div.querySelector(".position-buttons .top").addEventListener("click", () => {{
                div.classList.toggle("top");
                div.classList.toggle("bottom");
                localStorage.setItem("axs-audit-ask-position", "top");
            }})
            div.querySelector(".position-buttons .bottom").addEventListener("click", () => {{
                div.classList.toggle("top");
                div.classList.toggle("bottom");
                localStorage.setItem("axs-audit-ask-position", "bottom");
            }})
            return new Promise((resolve, reject) => {{
                let form = div.querySelector("form");
                form.onsubmit = evt => {{
                    evt.preventDefault();
                    resolve(event.submitter.value);
                    div.parentNode.removeChild(div);
                }}
            }});
        }}
    """
    )
    set_answer(element, question, answer)
    return answer


def init(page):
    page.add_style_tag(
        content="""
        #axs-audit-ask-container {
            all: initial;
            background-color: #f0f0fa;
            position: fixed;
            width: 100%;
            z-index: 99999;
            color: #0e152c;
        }
        #axs-audit-ask-container *, #axs-audit-ask-container *::after, #axs-audit-ask-container *::before {
            all: unset;
        }
        #axs-audit-ask-container .wrapper {
            padding: 10px;
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            gap: 2em;
            justify-content: space-between;
        }
        #axs-audit-ask-container.bottom {
            border-top: 5px solid #6e83d0;
            bottom: 0;
        }
        #axs-audit-ask-container.top {
            border-bottom: 5px solid #6e83d0;
            top: 0;
        }
        #axs-audit-ask-container form {
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            gap: 2em;
            margin-top: 10px;
        }
        #axs-audit-ask-container button {
            background-color: #6e83d0;
            color: #f0f0fa;
            padding: 5px;
            border-radius: 5px;
            border: 2px solid #6e83d0;
        }
        #axs-audit-ask-container button:hover {
            background-color: #f0f0fa;
            color: #6e83d0;
        }
        #axs-audit-ask-container.top .position-buttons .top {
            display: none;
        }
        #axs-audit-ask-container.bottom .position-buttons .bottom {
            display: none;
        }
    """
    )
