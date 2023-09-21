from sys import argv

assert len(argv) <= 2, "more than one argument provided"

assert argv[1].isnumeric(), "argument is not an integer"

num = int(argv[1])

if num % 2 == 0:
    print("I'm even")
else:
    print("I'm odd")
