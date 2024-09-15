def mail_chk(mail):
    try:
        tmp = 0
        for i in mail:
            if i == "@":
                tmp +=1
        if tmp == 0 or tmp > 1:
            return False
        mail = mail.split(".")
        var = ["net", "ru", "com"]
        for i in var:
            if i == mail[len(mail) - 1]:
                return True
        return False
    except Exception as e:
        return e

def send_email(message, recipient, sender="university.help@gmail.com"):
    recipient = recipient.lower()
    sender = sender.lower()
    if mail_chk(recipient) != True or mail_chk(sender) != True:
        return (f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')
    if recipient == sender:
        return "Нельзя отправить письмо самому себе!"
    if sender == "university.help@gmail.com":
        return (f'"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>')
    return (f'"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>')

print(
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'),
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'),
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'),
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'),
)
