#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for n in my_list:
            if x > num:
                print(n, end="")
                num += 1
        print()
        return num
    except IndexError:
        return num
