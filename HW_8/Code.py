#Переменные для подсчета результатов
right_answers = 0
user_points = 0
user_answers = []

#Задаем необходимые функции
def load_questions():
    """Загружает файл Json в Python"""
    import json
    with open("questions.json", "r") as file:
        file_json = file.read()
        all_questions = json.loads(file_json)
        return all_questions

def get_right_structure(word):
    """Формирует правильное окончание слова в зависимости от падежа"""
    if right_answers == 1:
        return word
    elif 2 <= right_answers <= 4:
        termination = "a"
        return word + termination
    elif right_answers >= 5:
        termination = "ов"
        return word + termination

def get_results():
    """Выводит результаты"""
    all_user_questions = len(user_answers)
    word_question = get_right_structure('вопрос')
    return f"Ну вот и все!\nОтвечено на {right_answers} {word_question} из {all_user_questions}.\nНабрано баллов: {user_points}."

#Вводим класс Вопрос и его методы
class Question:
    def __init__(self, text, complicity, right_answer):
        self.points = int(complicity) * 10
        self.complicity = complicity
        self.text = text
        self.right_answer = right_answer

    def get_points(self):
        return self.points

    def is_correct(self, answer=None):
        if self.right_answer == answer:
             return True
        else:
             return False

    def build_question(self):
         return f"Вопрос: {self.text}\nСложность {self.complicity}/5"

    def build_feedback(self, answer):
         if answer == self.right_answer:
             return f"Ответ верный, получено {self.points} баллов"
         else:
             return f"Ответ неверный, верный ответ {self.right_answer}"

#Основной код
print("Игра начинается!")
all_questions = load_questions()
for question in all_questions:
    question = Question(question['q'], question['d'], question['a'])
    print(question.build_question())
    user_answer = input()
    chosen_answer = question.is_correct(user_answer)
    user_answers.append(chosen_answer)
    if chosen_answer is True:
        points = question.get_points()
        user_points += points
        right_answers += 1
    print(question.build_feedback(user_answer))
print(get_results())

