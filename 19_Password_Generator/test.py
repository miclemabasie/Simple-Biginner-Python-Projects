from main import *

LOWER_LETTERS = string.ascii_lowercase
UPPER_LETTERS = string.ascii_uppercase
NUMBERS= string.digits
SPECIAL = '~!@#$%^&*()_+'

assert len(generatePassword(8)) != 12
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
print(pw)
for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
        print("haslower")
    if character in UPPER_LETTERS:
        hasUppercase = True
        print("hasupper")
    if character in NUMBERS:
        print("hasnumber")
        hasNumber = True
    if character in SPECIAL:
        print("hasspecial")
        hasSpecial = True

print(hasLowercase, hasUppercase, hasNumber, hasSpecial)
    # assert hasLowercase and hasUppercase and hasNumber and hasSpecial