import string as s
import secrets        #import the secret package 


def generate_password(length: int, symbols: bool, uppercase: bool):
    combination = s.ascii_lowercase + s.digits

    if symbols:
        combination += s.punctuation

    if uppercase:
        combination += s.ascii_uppercase

    combination_length = len(combination)

    new_password = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password


for _, index in enumerate(range(10)):     #pick from any of these 10 for your new password
    password = generate_password(length=18, symbols=True, uppercase=True)
    print(index + 1, ">>", password)
