import string
import random

def generatePassword(password_length):
    if password_length < 12:
        password_length = 12
    LOWER_LETTER = string.ascii_lowercase
    UPPER_LETTER = string.ascii_uppercase
    NUMBER = string.digits
    SPECIAL = '~!@#$%^&*()_+'
    CHARACTERS = LOWER_LETTER + UPPER_LETTER + NUMBER + SPECIAL
    upper = 0
    lower = 0
    number = 0
    special = 0
    trials = 1
    while True:
        password = ''
        print(f"Trials {trials}")
        for i in range(0, password_length):
            password += CHARACTERS[random.randint(0, len(CHARACTERS) - 1)]
        
        for letter in password:
            if letter in LOWER_LETTER:
                lower += 1
            if letter in UPPER_LETTER:
                upper += 1
            if letter in NUMBER:
                number += 1
            if letter in SPECIAL:
                special += 1
        if upper > 0 and lower > 0 and number > 0 and special > 0:
            return password
        trials += 1


def main():
    print(generatePassword(6))


if __name__ == "__main__":
    main()