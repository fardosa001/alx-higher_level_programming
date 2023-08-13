#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    num_args = len(argv)
    if num_args != 4:
        print('Usage:', argv[0], '<a> <operator> <b>')
        exit(1)

    operator = argv[2]
    p = {'+': add, '-': sub, '*': mul, '/': div}
    if operator not in p:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, p[operator](a, b)))
