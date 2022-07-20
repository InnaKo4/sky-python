#Запрашиваем имя пользователя
user_name = input("Введите ваше имя...")

#Импортируем библиотеку
import random

#Вводим функции
def get_listed_line(word):
    """Делает из слова список"""
    listed_word = []
    for w in word:
        if w != '\n':
            listed_word.append(w)
    return listed_word

def get_random_order(list):
    """Перемешивает буквы в слове"""
    random_list = random.shuffle(list)
    return random_list

#Основная работа с пользователем
user_points = 0
with open('words.txt') as file:
    for line in file:
        listed_line = get_listed_line(line)
        get_random_order(listed_line)
        print(f"Угадайте слово: {''.join(listed_line)}")
        user_answer = input()
        new_line = line.rstrip()
        if user_answer.lower() == new_line:
            print("Верно! Вы получаете 10 очков.")
            user_points += 10
        else:
            print(f"Неверно! Верный ответ – {new_line}.")

#Записываем ответы в новый файл
with open('history.txt', 'a') as file:
    content = file.write(f"{user_name} {user_points}\n")

#Подводим итоги
all_results = []
total_games = 0
with open('history.txt', 'r') as file:
    for f in file:
        gamer, points = f.rstrip().split(' ')
        total_games += 1
        all_results.append(points)
    print(f"Всего игр сыграно: {total_games}")
    print(f"Максимальный рекорд: {max(all_results)}")









