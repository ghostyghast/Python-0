from sys import argv
from string import punctuation


def find_punc(char):
    """find_punc(character)

check if the character given is punctuation
(based off of string.punctuation)
if so return 1, else 0"""
    for i in punctuation:
        if punctuation.find(i) >= 0:
            return 1
    return 0


def main():
    """main for the program that indicates number
of certain types characters in given string.
only 1 argument can be given, that being the string
(no argument results in input asked from the user)"""
    assert len(argv) <= 2, "Too many arguments"

    if len(argv) == 1:
        str = input("GIMME THE STRING BITCH :\n")
    else:
        str = argv[1]
    up, low, punc, space, digit, char = 0, 0, 0, 0, 0, 0
    for i in str:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
        elif i.isnumeric():
            digit += 1
        elif i.isspace():
            space += 1
        elif find_punc(i):
            punc += 1
        char += 1
    print(f"The text contains {char} characters:")
    print(f"{up} upper letters")
    print(f"{low} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


if __name__ == "__main__":
    main()
