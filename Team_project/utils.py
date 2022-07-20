import requests
import json
from basic_word import BasicWord
import random
def load_random_word():
    """Выбирает случайное слово из списка и возвращает его"""
    response = requests.get('https://jsonkeeper.com/b/5H2Y')
    list = json.loads(response.text)
    random_word = random.choice(list)
    basic_word = BasicWord(**random_word)
    return basic_word
