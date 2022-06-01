#!/usr/bin/python3
i = 0
for ord in range(122, 96, -1):
    print("{}".format(chr(ord - i)), end="")
    i = 32 if i == 0 else 0
