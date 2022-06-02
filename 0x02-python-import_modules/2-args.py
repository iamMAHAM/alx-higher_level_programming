#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length == 1 or length == 0:
        print("{} argument.".format(length))
    else:
        print("{} arguments:".format(length - 1))

    for i in range(length):
        print("{}: {}".format(i, argv[i])) if i != 0 else 0
