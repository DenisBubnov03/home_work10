from utils import *
from flask import Flask

app = Flask(__name__)
candidates_list = git_candidates()


@app.route("/")
def main_page():
    text = ""
    for candidate in candidates_list:
        text += "Имя кандидата - " + candidate["name"] + "\n"
        text += "Позиция кандидата - " + candidate["position"] + "\n"
        text += "Навыки: " + candidate["skills"] + "\n"
    return f"<pre>{text}</pre>"


@app.route("/candidates/<name>")
def candidate_page(name):
    for candidate in candidates_list:
        if name.title().strip() in candidate["name"].split(" "):
            return f'<center> <img src="{candidate["picture"]}" width="200" height="200" alt="">\n' \
                   f'<pre>Имя кандидата - {candidate["name"]}\n' \
                   f'Позиция кандидата - {candidate["position"]}\n' \
                   f'Навыки: {candidate["skills"]}</pre>'
        elif name.title().strip() == candidate["name"]:
            return f'<center> <img src="{candidate["picture"]}" width="200" height="200" alt="">\n' \
                   f'<pre>Имя кандидата - {candidate["name"]}\n' \
                   f'Позиция кандидата - {candidate["position"]}\n' \
                   f'Навыки: {candidate["skills"]}</pre>'
    return "Такого кандидата нет в базе"


@app.route("/candidates/<id>")
def candidate_page_id(pk):
    for candidate in candidates_list:
        if pk == candidate["id"]:
            return f'<center> <img src="{candidate["picture"]}" width="200" height="200" alt="">\n' \
                   f'<pre>Имя кандидата - {candidate["name"]}\n' \
                   f'Позиция кандидата - {candidate["position"]}\n' \
                   f'Навыки: {candidate["skills"]}</pre>'
    return "Такого кандидата нет в базе"


@app.route("/skills/<skills>")
def candidates_page(skills):
    skill = ""
    for candidate in candidates_list:
        if skills.lower().strip() in candidate["skills"].lower().split(", "):
            skill += "Имя кандидата - " + candidate["name"] + "\n"
            skill += "Позиция кандидата - " + candidate["position"] + "\n"
            skill += "Навыки: " + candidate["skills"] + "\n"
    if len(skill) == 0:
        return "Такого кандидата с умением нет в базе"
    return f"<pre>{skill}</pre>"


app.run()
