
def get_grade(grade):
    grade_dict = {2: "Плохо", 3: "Удовлетворительно", 4: "Хорошо", 5: "Отлично"}
    for k,v in grade_dict.items():
        if k == grade:
            return v
        else:
            return "Ошибка"
try:
    assert get_grade(2) == "Плохо"
    assert get_grade(3) == "Удовлетворительно"
    assert get_grade(4) == "Хорошо"
    assert get_grade(5) == "Отлично"
    assert get_grade("") == "Ошибка"
except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")
else:
    print("Все хорошо, все работает")


