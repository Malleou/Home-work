# здесь код


def num_skates(number: int) -> list:
    """Создаёт список размеров"""

    skates = []
    for num in range(number):
        size_skat = int(input(f'Размер {num + 1}-й пары: '))
        skates.append(size_skat)
    return skates




def sum_size(num: int) -> list:
    """Создаёт список размеров тех коньков, что взяли
    и сравнивает списки"""

    peoples = []
    for n in range(num):
        size_ppl = int(input(f'Размер ноги {n + 1}-го человека: '))
        if size_ppl in peoples:
            continue
        if size_ppl not in sk:
            print('Простите. у нас нет такого размера')
        else:
            peoples.append(size_ppl)
    return peoples




sum_skates = int(input('Кол-во коньков: '))
sk = num_skates(sum_skates)
print()
sum_peoples = int(input('Кол-во людей: '))
ppl = sum_size(sum_peoples)
print('Наибольшее кол-во людей, которые могут взять ролики:', len(sk) - len(ppl))