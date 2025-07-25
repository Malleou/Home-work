# TODO здесь писать код

def palindrome(word) -> bool:
    """Сравнивает символы в строке как ввели и в обратном порядке"""

    check = False
    counter = -1

    for i in word[::-1]:
        counter += 1
        for index, symbol in enumerate(word):
            if i.lower() == symbol.lower() and counter == index:
                check = True
    return check




word_check = input('Введите слово: ')
if palindrome(word_check):
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')