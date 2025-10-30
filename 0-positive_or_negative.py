#!/usr/bin/python3
import random

number = random.randint(-1000, 1000)

if not isinstance(number, int):
    print("wrong type")
elif number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
