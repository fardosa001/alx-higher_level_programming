#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    a_len = len(tuple_a)
    b_len = len(tuple_b)

    if a_len < 2:
        tuple_a = tuple_a + (0,) * (2 - a_len)
    if b_len < 2:
        tuple_b = tuple_b + (0,) * (2 - b_len)

    sum = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return sum
