def is_palindrome(word):
    other_word = []
    for w in word:
        if w != " ":
            other_word.append(w)
    new_word = "".join(other_word)
    reversed_word = new_word.lower
    if reversed_word == word[::-1]:
        return True
    else:
        return False

try:
    assert is_palindrome("level") == True
    assert is_palindrome("sagas") == True
    assert is_palindrome("hero") == False
    assert is_palindrome("drama") == False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")

else:
    print("Все хорошо, все работает")

