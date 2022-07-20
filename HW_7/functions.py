
def load_students():
    """Загружает данные из файла JSON в файл Python"""
    import json
    with open("students.json", "r") as file:
        file_json = file.read()
        students_data = json.loads(file_json)
        return students_data

def load_professions():
    """Загружает данные из файла JSON в файл Python"""
    import json
    with open("professions.json", "r") as f:
        file_json = f.read()
        professions_data = json.loads(file_json)
        return professions_data

def get_student_by_pk(pk):
    """Выводит данные о студенте по номеру"""
    students = load_students()
    for student in students:
        if student['pk'] == pk:
            return student

def get_profession_by_title(title):
    """Выводит данные о специальности по названию"""
    professions = load_professions()
    for profession in professions:
        if profession['title'] == title:
            return profession

def check_fitness(student, profession):
    """Выводит необходимые навыки, отсутствующие навыки и уровень пригодности для определенной специальности """
  student_skills = set(student['skills'])
  profession_skills = set(profession['skills'])
  student_has = student_skills.intersection(profession_skills)
  student_lack = profession_skills.difference(student_skills)
  total_student_skills = 0
  total_profession_skills = 0
  for ss in student_has:
      total_student_skills += 1
  for ps in profession_skills:
      total_profession_skills +=1
  fitness_percent = round(total_student_skills / total_profession_skills * 100)
  dict_skills = {"has": list(student_has), "lacks": list(student_lack), "fit_percent": fitness_percent}
  return dict_skills



















