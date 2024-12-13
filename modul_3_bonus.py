def all_sum(*args):
    """Функция принимает разные параметры и в зависимости и типа параметра,
    производит вычисление. Если есть числа, то складывает их, иначе находит длину и
    складывает её"""

    summ = 0

    for obj in args:
        if isinstance(obj, (int, float)):
            summ += obj
        elif isinstance(obj, str):
            summ += len(obj)
        elif isinstance(obj, dict):
            summ += all_sum(*obj.keys(), *obj.values())
        elif isinstance(obj, (list, tuple, set)):
            summ += all_sum(*obj)
    return summ




data_structure = [

[1, 2, 3],

{'a': 4, 'b': 5},

(6, {'cube': 7, 'drum': 8}),

"Hello",

((), [{(2, 'Urban', ('Urban2', 35))}])

]

print(all_sum(data_structure))