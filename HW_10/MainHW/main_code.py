#импортируем полезные функции
from flask import Flask
from functions import load_candidates
from functions import get_all
from functions import get_by_pk
from functions import get_by_skill

#основное тело функции
candidates = load_candidates()
app = Flask(__name__)

#создаем главную страницу
@app.route("/")
def main_page():
    all_candidates = get_all(candidates)
    new_candidates = '\n'.join(all_candidates)
    return new_candidates

#создаем страницу для каждого кандидата по его номеру
@app.route("/candidates/<int:x>")
def candidate_page(x):
    candidate = get_by_pk(x)
    name = candidate['name']
    position = candidate['position']
    skills = candidate['skills']
    url = candidate ['picture']
    return f"<img src='({url})'>\n<pre>\n{name}\n{position}\n{skills}</pre>"

#создаем страницу для данных о кандидатах по их навыку
@app.route('/skills/<x>')
def skills_page(x):
    users_with_skill = get_by_skill(x)
    all_users = '\n'.join(users_with_skill)
    return all_users

app.run(host='127.0.0.1', port=7000)












