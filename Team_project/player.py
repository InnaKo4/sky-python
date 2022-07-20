class Player:
    def __init__(self, name):
        """Иницилизирует класс"""
        self.name = name
        self.user_words = []

    def __repr__(self):
        return 'Игрок'

    def counter(self):
        """Подсчитывает количество угаданных слов """
        return len(self.user_words)

    def add_word(self, word):
        """Добавляет слово в список угаданных слов игрока"""
        self.user_words.append(word)

    def check_used_word (self, word):
        """Проверяет, есть ли слово в списке угаданных слов"""
        if word in self.user_words:
            return True
        else:
            return False