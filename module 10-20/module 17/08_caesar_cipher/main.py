# здесь код

def coder(text: str, shift: int) -> str:
    """Шифрует введённое сообщение ао шифру Цезаря
    С сохранением регистра и пропускает символы, которые не входят в алфавит"""

    abc_low = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    abc_up = abc_low.upper()
    shift %= len(abc_low)
    code_message = ''

    code_list = [abc_low[(abc_low.index(sym) + shift) % len(abc_low)] if sym in abc_low else
                 abc_up[(abc_up.index(sym) + shift) % len(abc_up)] if sym in abc_up else sym
                 for sym in text]

    for symbol in code_list:
        code_message += symbol

    # for sym in text:
    #     if sym not in abc_low and abc_up:
    #         new_text += sym
    #         continue
    #     elif sym in abc_low:
    #         ind = (abc_low.index(sym) + shift) % len(abc_low)
    #         new_text += abc_low[ind]
    #     else:
    #         ind = (abc_up.index(sym) + shift) % len(abc_up)
    #         new_text += abc_up[ind]

    return code_message

message = input('Введите сообщение: ')
num = int(input('Введите сдвиг: '))
print('Зашифрованное сообщение:', coder(message, num))