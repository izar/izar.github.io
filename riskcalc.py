import js
from js import document, console

target = "riskcalc"
status_msg = ["No", "Yes"]
questions = []

question_template = Element("question-template").select(".question", from_content=True)
question_list = [Element("list-container-0"), Element("list-container-1")]


# one state per question
state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def add_question(target_list=0, *args, **kws):
    if not question_msg:
        return None

    question_id = f"q_{len(questions)}"
    question = {
        "id": question_id,
        "content": question_msg,
        "state": 0,
        "input": None
    }

    questions.append(question)

    question_html = question_template.clone(question_id, to=question_list[target_list])
    question_html_content = question_html.select("p")
    question_html_content.element.innerText = question["content"]
    question_list[target_list].element.appendChild(question_html.element)
    question_html_check = question_html.select("input")
    question["input"] = question_html_check

    def check_question(evt=None):
        error_area = document.getElementById('error')
        error_content = Element("error").select("p")
        error_content.element.innerText = " "
        error_area.setAttribute('style', 'background-color: #e9ecef')
        
        question["state"] = 1 - question["state"]
        vector = "".join([str(q["state"]) for q in questions])
        vector_d = int(f"0b{vector}", base=2)
        out_content = Element("vector").select("p")
        out_content.element.innerText = f"LalalaRiskV0.1:{vector_d}"
        
        # can't have q1 be true AND q>1 also be true at the same time
        if vector_d > 2**(len(questions)-1):
            error_content.element.innerText = "It's an OR situation. Please unselect."
            question["input"].checked = False                        
            error_area.setAttribute('style', 'background-color: #ff3300')
            return
        else:
            error_content.element.innerText = " "


    question_html_check.element.onclick = check_question
    


questions_1 = {
    "1":  "Will the software / vendor / process need to connect to the internet to function or store its data on the cloud?"
}

questions_2 = {	
"2": "Will the Software / Vendor access Lalala financial systems or handle / access / store Lalala financial data?",
"3": "Will the Software / Vendor handle, access, or store Employee Personal Data?",
"4": "Will the Software / Vendor handle, access, or store Customer Personal Data?",
"5": "Will the Software / Vendor access Lalala build systems?",
"6": "Will the Software / Vendor handle authentication and/or authorization of employee, customer or system accounts ?",
"7": "Will the Software / Vendor handle, access, or store Secrets: keys, API keys, cookies, passwords, etc.?",
"8": "Wiil the Software / Vendor get remote access to Lalala assets?",
"9": "Will the Software / Vendor gain physical access to Lalala assets?",
"10": "Will the Software / Vendor require integration with Slack / Pagerduty / Gmail?",
"11": "Will the Software / Vendor handle, access, or store Lalala source code?",
"12": "Will the Software / Vendor handle, access, or store confidential company data ?",
}

# first side of the OR
for idx in questions_1:
    question_msg = questions_1[idx]
    add_question(question_msg = question_msg, target_list=0)

# second side of the OR
for idx in questions_2:
    question_msg = questions_2[idx]
    add_question(question_msg = question_msg, target_list=1)

