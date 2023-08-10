#!/usr/bin/python3
for j in reversed(range(97, 123)):
    print("{:c}".format(j - 32 if j % 2 != 0 else j), end="")
