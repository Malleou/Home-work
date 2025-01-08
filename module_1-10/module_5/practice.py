class Database:

    def __init__(self):

        self.data = {}



    def add_user(self, username, password):

        self.data[username] = password


class User:
    """
    Класс пользователя, пользователя содержащий: логин, пароль
    """
    def __init__(self, username, password, password_confirmation):

        self.username = username
        if password  == password_confirmation:
            self.password = password



def valid_pass(password: str):

    len_ = True
    if len(password) < 8:
        len_ = False
    up = any(sym.isupper() for sym in password)
    low = any(sym.islower() for sym in password)
    num = any(sym.isdigit() for sym in password)
    return len_ and up and low and num



if __name__ == '__main__':
    database = Database()

    while True:
        choice = int(input('Приветствую! Выберете действие:\n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('Пользователь не найден')
        if choice == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password2 := input('Повторите пароль: '))
            if not valid_pass(user.password):
                print('Пароль должен состоять из латинских заглавных и строчных букв,'
                      'а так же, содержать хотя бы одну цифру')
                continue
            else:
                if password != password2:
                    print('Пароли не совпадают. Попробуйте ещё раз')
                    continue
            database.add_user(user.username, user.password)
        print(database.data)