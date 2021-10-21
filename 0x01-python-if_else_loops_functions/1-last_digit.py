#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    nums = number % 10
    if nums == 0:
        print(f"Last digit of {number} is {nums} and is zero")
    elif nums < 5:
        print(f"Last digit of {number} is {nums} and is less than 5")
    else:
        print(f"Last digit of {number} is {nums} and is greater than 5")
else:
    n = number * -1
    nums = n % 10
    if nums == 0:
        print(f"Last digit of {number} is {nums} and is zero")
    elif nums < 5:
        print(f"Last digit of {number} is {nums} and is less than 5")
    else:
        print(f"Last digit of {number} is {nums} and is greater than 5")
