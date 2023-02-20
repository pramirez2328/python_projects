'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/19/2023
Homework Problem # 5_3
Description:
Write a python program without a function that does the following: 
Prompts the user to enter four numbers in one request.
Use that input to perform the following calculation: 
Multiply the first number by the second number, 
then add that result to the third number, and finally, 
divide the result by the fourth number.
This program MUST NOT CRASH. 
To insure this you must validate the input data and calculations: 
• Checking the user entered four values 
• Appropriately checking for the following errors: 
ValueError, ZeroDivisionError, IndexError. 
'''

input_message = "Enter 4 integers, separated by comas: "
result = 0
formula = ""

while True:
    try:
        user_input = input(input_message).split(',')
        # validate input for 4 integers
        first_int = int(user_input[0])
        second_int = int(user_input[1])
        third_int = int(user_input[2])
        fourth_int = int(user_input[3])
        result = (first_int * second_int + third_int) / fourth_int
        # collects the formula for printing
        formula = f"({first_int} * {second_int} + {third_int}) / {fourth_int}"
    except ValueError as value_error:
        print("\n--- Invalid input. Please try again.", value_error)
        continue
    except IndexError as index_error:
        print("\n--- Invalid input. Please try again.", index_error)
        continue
    except ZeroDivisionError as zero_division_error:
        print("\n--- Invalid input. Please try again.", zero_division_error)
        continue
    else:
        break

# print the formula and result
print(f"\n{formula} = {result}")
