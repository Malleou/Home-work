# TODO здесь писать код

def containers(sum_containers) -> list:
    """Создаёт список контейнеров"""

    range_containers = []

    print()
    for _ in range(sum_containers):
        container: int = int(input('Введите вес контейнера: '))
        if container >= 200:
            print('Ошибка! Масса контейнера не должна превышать 200')
            continue
        else:
            range_containers.append(container)
    print()
    return range_containers




def new_container(range_containers) -> int:
    """Сортирует список и находит нужное место по индексу"""

    new_cont: int = int(input('Введите вес нового контейнера: '))
    while new_cont >= 200:
        print('Ошибка! Масса контейнера не должна превышать 200')
        new_cont: int = int(input('Ещё раз, введите вес нового контейнера: '))
    range_containers.append(new_cont)
    range_containers.sort(reverse = True)
    for index, mass in enumerate(range_containers):
        if mass == new_cont:
            place: int = index + 1
            return place

sum_cont: int = int(input('Количество контейнеров: '))
new_num = new_container(containers(sum_cont))
print('Номер, который получит новый контейнер:', new_num)