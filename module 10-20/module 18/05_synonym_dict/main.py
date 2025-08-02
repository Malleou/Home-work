# здесь код
def synonyms(txt: str, dict_synonyms: dict) -> dict:
    """Создаёт словарь синонимов"""

    txt_list = txt.split()
    dict_synonyms.update({txt_list[0]: txt_list[2]})
    return dict_synonyms



def search_synonyms(syn: dict, word: str) -> str:
    """Проверка, есть ли синоним в словаре"""

    word = word[0].upper() + word[1:].lower()
    if word in syn:
        return f'Синоним: {syn[word]}'
    elif word in syn.values():
        for key in syn:
            if syn[key] == word:
                return f'Синоним: {key}'
    else:
        return 'Такого слова в словаре нет.'



d_syn = dict()
num = int(input('Введите количество пар слов: '))
for i in range(num):
    text = input(f'{i + 1} пара: ')
    synonyms(text, d_syn)
print()
search = input('Введите слово: ')
while search != 'END':
    print(search_synonyms(d_syn, search))
    search = input('Введите слово: ')

