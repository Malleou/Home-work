# здесь код
def histogram(txt: str) -> dict:
    """Создание гистограммы"""

    txt_dict = dict()
    for sym in txt:
        if sym in txt_dict:
            txt_dict[sym] += 1
        else:
            txt_dict[sym] = 1
    return txt_dict



def revers_histogram(hist: dict) -> dict:
    """Меняет местами ключи и значения"""

    r_hist = dict()
    for key, value in hist.items():
        if value not in  r_hist:
            r_hist[value] = []
        r_hist[value].append(key)

    return r_hist


text = input('Введите текст: ')

text_dict = histogram(text)
print('Оригинальный словарь частот:')
for key in text_dict:
    print(key, ':', text_dict[key])

rev_hist = revers_histogram(text_dict)
print('Инвертированный словарь частот:')
for k in rev_hist:
    print(k, ':', rev_hist[k])