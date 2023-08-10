#!/usr/bin/python3
for j in reversed(range(97, 123)):
    if j % 2 == 0:
        print(f"{j:c}", end="")
    else:
        print(f"{j - 32:c}", end="")
