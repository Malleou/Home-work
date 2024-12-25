def control(email):
    counter = 0
    domains_test = ['.ru', '.com', '.net']
    boolean = False

    for domain in domains_test:  # Поиск нужного домена
        if email[-len(domain):] == domain:
            boolean = True
            break
    for dog in email:  # Подсчёт символа @
        if dog == '@':
            counter += 1
    if counter != 1:
        boolean = False
    return boolean


def send_email(massage, recipient, *, sender = 'university.help@gmail.com'):
    #recipient = recipient.lower()
    #sender = sender.lower()
# Выполнение условий задачи:
    if control(recipient) == False or control(sender) == False:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    elif sender != 'university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
           sender = 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
           sender = 'urban.teacher@mail.ru')