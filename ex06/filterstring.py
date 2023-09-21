from sys import argv
from string import punctuation


def correct_arg(string):
    for i in string:
        if punctuation.find(i) != -1:
            return False
    if string.isprintable() is False:
        return False
    return True


def func(x, num):
    return lambda x, num: True if len(x) > num else False


def filterstring(string, num):
    words = string.split()
    new_lst = [x for x in words if func(x, num)]
    return (new_lst)


def main():
    assert len(argv) == 3, "invalid argument amount"
    assert argv[2].isalpha, "arguments invalid"
    assert correct_arg(argv[1]), "arguments invalid"
    print(filterstring(argv[1], int(argv[2])))


if __name__ == "__main__":
    main()
