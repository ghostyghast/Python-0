from sys import argv
import string


def main():
    assert len(argv) <= 2, "Too many arguments"

    if len(argv) == 1:
        str = input("GIMME THE STRING BITCH\n")
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
        elif i.isalnum() is False:
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
