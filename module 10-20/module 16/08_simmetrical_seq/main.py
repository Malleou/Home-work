# здесь код



def new_list(add_num: int) -> list:
    """Создаёт новый список из чисел"""

    list_ = []

    for _ in range(add_num):
        num = int(input('Число: '))
        list_.append(num)
    return list_




def is_mirror(list_: list) -> bool:
    """Проверка на идентичность"""
    revers_list = []

    for i_num in range(len(list_) -1, -1, -1):
        revers_list.append(list_[i_num])
    if  list_ == revers_list:
        return True
    else:
        return False



add = int(input('Кол-во чисел: '))
num_list = new_list(add)

miss_num = []

answer = []
for i_nums in range(0, len(num_list)):
    for j_nums in range(i_nums, len(num_list)):
        miss_num.append(num_list[j_nums])
    if is_mirror(miss_num):
        for i_answer in range(0, i_nums):
            answer.append(num_list[i_answer])
        answer.reverse()
        break
    miss_num = []

print('Последовательность:', num_list)
print('Нужно приписать чисел:', len(answer))
print('Сами числа:', answer)