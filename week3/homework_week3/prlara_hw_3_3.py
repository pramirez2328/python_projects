'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/6/2023
Homework Problem # 3_3
Description:
Prompt users to enter a three-digit whole number,
the digits must be in ascending order and without duplicates.
'''
# ask user to enter a 3 digit number
three_digit_number = input("Please enter a 3-digit integer: ")

condition = True
while condition:
    # check if the number is a 3 digit number
    numeric = three_digit_number.isnumeric()

    # check if the number is a 3 digit number
    size = len(three_digit_number) == 3

    # check if the number has duplicates
    duplicate = len(set(three_digit_number)) != 3

    # check if the number is in ascending order
    ascending = False
    if numeric and size and not duplicate:
        list_of_digits = list(map(int, three_digit_number))
        ascending = list_of_digits[0] < list_of_digits[1] < list_of_digits[2]

    if not numeric:
        print('Error: This is not an integer. Please re-enter.')
    elif not size:
        print('Error: You did not enter a 3-digit number.')
    elif duplicate:
        print('Error: Your number contains duplication.')
    elif not ascending:
        print('Error: The digits are not in ascending order.')
    else:
        print('Number accepted.')
        break
    three_digit_number = input("Please enter a 3-digit number: ")
