import re


def email_parse(email):
    RE_EMAIL = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not RE_EMAIL.match(email):
        raise ValueError(f'wrong email: {email}')
    print(RE_EMAIL.match(email).groupdict())


user_email = input('Введите свой Email: ')
email_parse(user_email)
