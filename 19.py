import random

NUMBERS = '0123456789'
SPECIAL = '~!@#$%^&*()_+'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
COMBINATION = NUMBERS + SPECIAL + UPPER_LETTERS + LOWER_LETTERS


def generatePassword(length):
    if length < 12:
        length = 12

    password = []
    password.append(LOWER_LETTERS[random.randint(0, 25)])
    password.append(UPPER_LETTERS[random.randint(0, 25)])
    password.append(NUMBERS[random.randint(0, 9)])
    password.append(SPECIAL[random.randint(0, 12)])
    while len(password) < length:
        password.append(COMBINATION[random.randint(0, 74)])
    random.shuffle(password)

    return ''.join(password)


assert len(generatePassword(8)) == 12

 

pw = generatePassword(14)

assert len(pw) == 14

hasLowercase = False

hasUppercase = False

hasNumber = False

hasSpecial = False

for character in pw:

    if character in LOWER_LETTERS:

        hasLowercase = True

    if character in UPPER_LETTERS:

        hasUppercase = True

    if character in NUMBERS:

        hasNumber = True

    if character in SPECIAL:

        hasSpecial = True

assert hasLowercase and hasUppercase and hasNumber and hasSpecial
