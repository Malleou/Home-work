# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)

# переписать программу

def list_1(list_a, list_b: list) -> (list, int):
    """Объединяет 2 списка, считает количество цифр 5 и удаляет их из списка"""

    list_a.extend(list_b)
    counter1 = list_a.count(5)

    for _ in range(counter1):
            list_a.remove(5)
    return list_a, counter1




def list_2(list_a, list_c: list) -> (list, int):
    """Объединяет 2 списка, считает количество цир 3"""

    list_a.extend(list_c)
    counter2 = list_a.count(3)
    return list_a, counter2




a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
list_, count1 = list_1(a,b)
fin_list_, count2 = list_2(list_, c)
print('Количество цифр 5 при первом объединении:', count1)
print('Количество цифр 3 при втором объединении:', count2)
print('Итоговый список:', fin_list_)