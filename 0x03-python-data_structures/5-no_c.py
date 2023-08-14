#!/usr/bin/python3
def no_c(my_string):
    newStr = ''
    for j in my_string:
        if j != 'C' and j != 'c':
            newStr += j
    return newStr
