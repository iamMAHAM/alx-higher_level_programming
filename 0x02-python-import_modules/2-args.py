#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    length = len(argv[1:])
    if length == 1:
        print("{} argument.".format(length))
        exit(0)
    else:
        print("{} arguments:".format(length))

    for i in range(length + 1):
        print("{}: {}".format(i, argv[i])) if i != 0 else 0
