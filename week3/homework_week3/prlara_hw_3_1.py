'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/6/2023
Homework Problem # 3_1
Description:
Write a program that will iterate through the numbers from 2 to 130,
if it is even, count it and keep track of the first and last even number.
if it is odd, count it and keep track of the first and last odd number.
if it is a perfect square, count it and append it to a list of squares.
if it is a perfect cube, count it and append it to a list of cubes.
'''

import math

# Constants
START = 2
END = 130

# Variables
first_odd, last_odd, first_even, last_even = 0, 0, 0, 0
total_number_of_squares = 0
total_number_of_cubes = 0
total_number_of_odds = 0
total_number_of_evens = 0
squares, cubes = [], []

# iterate through the numbers from 2 to 130
for i in range(START, END + 1):
    # if it is even, count it and keep track of the first and last even number.
    if i % 2 == 0:
        total_number_of_evens += 1
        if first_even == 0:
            first_even = i
        last_even = i
    # if it is odd, count it and keep track of the first and last odd number.
    else:
        total_number_of_odds += 1
        if first_odd == 0:
            first_odd = i
        last_odd = i

    # if it is a perfect square, count it and append it to a list of squares.
    if math.sqrt(i).is_integer():
        total_number_of_squares += 1
        squares.append(i)

    # if it is a perfect cube, count it and append it to a list of cubes.
    root_cube = round(math.pow(i, 1 / 3))
    if root_cube**3 == i:
        total_number_of_cubes += 1
        cubes.append(i)

print()
print(f'Checking numbers from {START} to {END}')
print(f'Odd ({total_number_of_odds}): {first_odd}...{last_odd}')
print(f'Even ({total_number_of_evens}): {first_even}...{last_even}')
print(f'Square ({total_number_of_squares}): {squares}')
print(f'Cube ({total_number_of_cubes}): {cubes}')
