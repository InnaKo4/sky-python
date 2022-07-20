#Импортируем классы и функции
from player import Player
from utils import load_random_word

#Начинаем основной код с приветствия
print("Добро Пожаловать!\nВведите имя игрока: ")
user_name = input()
player = Player(user_name)
print(f"Привет, {player.name}!")

#Переносим файл Json в Python
new_word = load_random_word()
all_words = new_word.count_words()
print(f"Составьте {all_words} слов из слова {new_word.word.upper()}.")
print('Слова должны быть не короче 3 букв!\n')
print(f"Чтобы закончить игру, угадайте все слова или напишите 'stop'.\nПоехали, ваше первое слово?")
#Запускаем цикл
for i in range(all_words):
    input_word = input()
    user_word = input_word.lower()
    if user_word == "stop":
        print(f"Игра завершена!\nВы угадали: {player.counter()} слов")
        quit()
    elif len(user_word) < 3:
        print("Слишком короткое слово!")
    elif new_word.check_word(user_word) is False:
        print("Неверно.")
    elif player.check_used_word(user_word) is True:
        print("Уже использовалось!")
    else:
        print("Верно. Хорошее слово!")
        player.add_word(user_word)

print(f"Игра завершена!\nВы угадали: {player.counter()} слова")

