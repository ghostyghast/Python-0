from sys import argv


def parse(string):
    for i in string:
        if i.isalnum() is False and i != ' ':
            return False
    return True


def main():
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
