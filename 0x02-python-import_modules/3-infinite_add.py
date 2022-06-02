#!/usr/bin/python3
from sys import argv

def add():
    sum = 0
    for i in range(len(argv)):
        sum += int(argv[i]) if i > 0 else 0
    return sum

if __name__ == "__main__":
    print(add())