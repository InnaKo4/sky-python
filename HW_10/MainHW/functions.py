# полезные функции
import json

def load_candidates():
    """Загружает данные из Json в Python"""
    with open("candidates.json", "r") as file:
        file_json = file.read()
        all_candidates = json.loads(file_json)
        return all_candidates


def get_all(candidates):
    """Получает весь список кандидатов в виде списка"""
    new_candidates = []
    for candidate in candidates:
        name = candidate['name']
        position = candidate['position']
        skills = candidate['skills']
        candidate_information = f'<pre>\n{name}\n{position}\n{skills}\n'
        new_candidates.append(candidate_information)
    return new_candidates


def get_by_pk(pk):
    """Получает данные кандидата по его номеру"""
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate

def get_by_skill(skill_name):
    """Получает данные кандидатов по навыку и выводит в виде списка"""
    skill_owned = []
    candidates = load_candidates()
    for candidate in candidates:
        candidates_skills = candidate['skills'].lower().split(',')
        if skill_name.lower() in candidates_skills:
            name = candidate['name']
            position = candidate['position']
            skills = candidate['skills']
            skill_information = f'<pre>\n{name}\n{position}\n{skills}'
            skill_owned.append(skill_information)
    return skill_owned
