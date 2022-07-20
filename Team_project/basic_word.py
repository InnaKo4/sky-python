class BasicWord:
    def __init__(self, word, subwords):
        """Иницилизирует класс"""
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return "Основное слово"

    def check_word(self, word):
        """Проверяет наличие слова в списке подслов и выведит True или False"""
        if word in self.subwords:
            return True
        else:
            return False

    def count_words(self):
        """Выводит количество подслов"""
        return len(self.subwords)





