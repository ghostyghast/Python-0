from sys import argv
from string import punctuation
from ft_filter import ft_filter


def correct_arg(string):
    for i in string:
        if punctuation.find(i) != -1:
            return False
    if string.isprintable() is False:
        return False
    return True


def func(x, num):
    return lambda x, num: True if len(x) > num else False


def main():
    assert len(argv) == 3, "invalid argument amount"
    assert argv[2].isalpha, "arguments invalid"
    assert correct_arg(argv[1]), "arguments invalid"
    print(ft_filter(lambda word, num=int(argv[2]): len(word) > num, argv[1].split()))


if __name__ == "__main__":
    main()
