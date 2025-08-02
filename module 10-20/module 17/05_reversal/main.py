# здесь код

def text_slice(text: str) -> str:
    """Находит отрывок между двумя 'h'"""

    first = text.index('h')
    second = text.rindex('h')
    revers_slice = text[second -1: first: -1]
    return revers_slice



txt = input('Введите строку: ')
print('Развёрнутая последовательность между первым и последним h:', text_slice(txt))