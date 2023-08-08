#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f'{number:0} is positive')
elif number == 0:
    print(f'{number:0} is zero')
elif number < 0:
    print(f'{number:0} is negative')
