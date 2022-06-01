#!/usr/bin/python3
from copyreg import constructor


str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str.index("h "))
str = f"{str[39:67]}{str[107:112]}{str[114:112]}{str[:6]}"
print(str)

