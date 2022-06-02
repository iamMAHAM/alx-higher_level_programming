#!/usr/bin/python3

from sys import argv

length = len(argv) - 1
if length == 1 or length == 0:
    print(f"{length} argument.")
else:
    print(f"{length} arguments:")

for i in range(length + 1):
    print(f"{i}: {argv[i]}") if i != 0 else 0
