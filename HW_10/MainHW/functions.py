# полезные функции
import json


def load_candidates():
    with open("candidates.json", "r") as file:
        file_json = file.read()
        all_candidates = json.loads(file_json)
        return all_candidates


def get_all(candidates):
    new_candidates = []
    for candidate in candidates:
        name = candidate['name']
        position = candidate['position']
        skills = candidate['skills']
        candidate_information = f'<pre>\n{name}\n{position}\n{skills}'
        new_candidates.append(candidate_information)
    return new_candidates


def get_by_pk(pk):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate

def get_by_skill(skill_name):
    skill_owned = []
    candidates = load_candidates()
    for candidate in candidates:
        new_skills = candidate['skills'].lower()
        if skill_name in new_skills:
            name = candidate['name']
            position = candidate['position']
            skills = candidate['skills']
            skill_information = f'<pre>\n{name}\n{position}\n{skills}'
            skill_owned.append(skill_information)
    return skill_owned
