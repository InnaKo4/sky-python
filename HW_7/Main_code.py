#Импортируем необходимые нам функции
from functions import get_student_by_pk
from functions import get_profession_by_title
from functions import check_fitness

#Начинаем работу с основным кодом
#Выбираем студента по pk
print("Введите номер студента")
user_pk = input()
student = get_student_by_pk(user_pk)
if student is None:
    print("У нас нет такого студента.")
    quit()
else:
    student_name = student['full_name']
    student_skills = ", ".join(student['skills'])
    print(f"Студент {student_name}\nЗнает {student_skills}")

#Работаем со специальностью
print(f"Выберите специальность для оценки студента {student_name}")
chosen_profession = input()
new_profession = chosen_profession.title()
profession = get_profession_by_title(new_profession)
if profession is None:
    print("У нас нет такой специальности.")
    quit()
else:
    dict_student_skills = check_fitness(student, profession)
    student_skills = ", ".join(dict_student_skills['has'])
    students_lacks = ", ".join(dict_student_skills['lacks'])
    fitness_percent = dict_student_skills['fit_percent']
    if fitness_percent == 0:
        print(f"Пригодность {fitness_percent}%")
        print(f"Студент {student_name} не обладает необходимыми для данной специальности навыками")
    elif fitness_percent == 100:
        print(f"Пригодность {fitness_percent}%")
        print(f"{student_name} знает {student_skills}")
    else:
        print(f"Пригодность {fitness_percent}%")
        print(f"{student_name} знает {student_skills}")
        print(f"{student_name} не знает {students_lacks}")







