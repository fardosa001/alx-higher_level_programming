#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = argv[1:]
    num_args = len(args)

    if num_args == 1:
        print(num_args, 'argument:')
        for i, arg in enumerate(args, start=1):
            print('{:d}: {}'.format(i, arg))
    elif num_args > 1:
        print(num_args, 'arguments:')
        for i, arg in enumerate(args, start=1):
            print('{:d}: {}'.format(i, arg))
    elif num_args == 0:
        print(num_args, 'arguments.')
