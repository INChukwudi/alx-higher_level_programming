#!/usr/bin/python3
i = 32
for letter in range(97, 123, -1):
    print("{}".format(chr(letter - i)), end="")
    i = 32 if i == 0 else 0
