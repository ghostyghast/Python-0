from sys import argv
from string import punctuation
from ft_filter import ft_filter


def correct_arg(string):
    """correct_arg(phrase given as argyment) --> Bool
    takes argument from main and
        returns true if all arguments are valid
        (all characters are printable and no punctuation)"""
    for i in string:
        if punctuation.find(i) != -1:
            return False
    if string.isprintable() is False:
        return False
    return True


def main():
    """program that splits words and prints the ones
    that are longer than the int given second argument.
    prints an assetion error if invalid arguments
    (words have unprintable or punctuation characters,
    or argument amount is not 2)"""

    assert len(argv) == 3, "invalid argument amount"
    assert argv[2].isalpha, "arguments invalid"
    assert correct_arg(argv[1]), "arguments invalid"
    words = argv[1].split()
    print(ft_filter(lambda word, num=int(argv[2]): len(word) > num, words))


if __name__ == "__main__":
    main()
