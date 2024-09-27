def send_email(messages, recipient:str, sender = 'university.help@gmail.com'):
    if recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net')):
        if '@' not in recipient or "@" not in sender:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            return #завершаем выполнение фукции
    else:  #либо у получателя либо у отправителя
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    if recipient == sender:
        print('Нельзя отправить сообщение самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправленно с адреса {sender} на адрес {recipient}')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')






send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')