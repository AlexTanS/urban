def send_email(message, recipient, *, sender="university.help@gmail.com"):
    is_true_mail = False
    result = ''
    if "@" in recipient and "@" in sender:
        is_true_mail = True
    if (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')) and (
            sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')):
        if is_true_mail:
            if recipient.upper() == sender.upper():
                result = 'Нельзя отправить письмо самому себе!'
            elif sender == 'university.help@gmail.com':
                result = f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.'
            else:
                result = f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.'
    else:
        result = f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.'
    print(result)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

