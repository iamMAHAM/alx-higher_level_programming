#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    length = len(argv[1:])
    if length == 1:
        print("{:d} argument:".format(length))
    elif length == 0:
        print("0 arguments.")
        exit(0)
    else:
        print("{} arguments:".format(length))

    for i in range(1, length + 1):
        print("{:d}: {}".format(i, argv[i]))
