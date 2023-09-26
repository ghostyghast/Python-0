from sys import argv


def parse(string):
    """parse(string) --> Bool
    checks if string contains only alphanumeric
    chracters"""
    for i in string:
        if i.isalnum() is False and i != ' ':
            return False
    return True


def main():
    """program that takes a string of alphanumeric characters
    and prints it back out in morse code.
    Raise an assertion error if argument amount is not 2 and
    string contains only alphanum characters """
    assert len(argv) == 2, "invalid argument count"
    assert parse(argv[1]), "invalid string"
    morse = {" ": "/",
             "A": ".- ", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
             'J': '.---', 'K': '.-..', 'L': '.-..', 'M': '--',
             'N': '-.', 'O': '---', 'P': '.---.', 'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
             'V': '..-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
             'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....', '7': '--...',
             '8': '---..', '9': '----.', '0': '-----'}
    for x in argv[1]:
        print(morse[x.upper()], end=' ')


if __name__ == "__main__":
    main()
