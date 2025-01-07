import time

class User:

    def __init__(self, nickname, password, age):

        self.nickname = nickname
        self.age = age
        self.password = hash(password)



class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False):

        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode




# def valid_password(password: str):
#
#     len_ = True
#     if len(password) < 8:
#         len_ = False
#     up = any(sym.isupper() for sym in password)
#     low = any(sym.islower() for sym in password)
#     num = any(sym.isdigit() for sym in password)
#     return len_ and up and low and num




class UrTube:

    current_user = None

    def __init__(self):
        self.users = {}
        self.videos = []



    def log_in(self, login, password):

        if login in self.users:
            if self.users[login][0] == hash(password):
                self.current_user = login
                print(f'Здравствуйте, {self.current_user}!')
            else:
                print('Неверный пароль')
        else:
            print('Пользователь с таким именем не найден')



    def register(self, nickname, password, age):

        progress = False

        if nickname in self.users:
            print('\nНикнейм уже занят')
        # if not valid_password(password):
        #     print('\nДлина пароля должна быть не менее 8 символов,'
        #           'пароль должен состоять из заглавных, строчных букв и цифр')
        #     return False
        else:
            self.users[nickname] = (hash(password), age)
            print(f'\n{nickname} успешно зарегистрирован')
            progress = True
        return progress



    def log_out(self):
        if self.current_user:
            print(f'Вы вышли из аккаунта {self.current_user}')
            self.current_user = None



    def add(self):
        title = input('Введите название видео: ')
        duration = int(input('Введите продолжительность видео в секундах: '))
        time_now = 0
        choice = int(input('Установить возрастное ограничение?\n1 - Да\n2 - Нет\n'))
        if choice == 1:
            adult_mode = True
        else:
            adult_mode = False
        if any(video.title == title for video in self.videos):
            print('Видео с таким названием уже существует')
            return
        self.videos.append(Video(title, duration, time_now, adult_mode))
        print(f'Видео {title} успешно добавлено')



    def get_videos(self, search_text):

        search_text = search_text.lower()
        return [video.title for video in self.videos if search_text  in video.title.lower()]



    def watch_video(self, name_video):

        wid_to_watch = next((video for video in self.videos if video.title == name_video), None)

        if wid_to_watch:
            if self.current_user:
                if wid_to_watch.adult_mode and self.users[self.current_user][1] >= 18:
                    print('\nПриятного просмотра!')
                    print('время видео:')
                    for i in range(1, wid_to_watch.duration + 1):
                        print(i, end=' ')
                        wid_to_watch.time_now += 1
                        time.sleep(1)
                    print('Конец видео')
                else:
                    print('\nВам нет 18-ти лет. Пожалуйста покиньте страницу')
            else:
                print('\nВойдите в аккаунт, чтобы смотреть видео')
        else:
            print('\nВидео не найдено')




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add()
ur.add()

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')