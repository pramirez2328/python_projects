'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/19/2023
Homework Problem # 5_5
Description:
Write a python program that does the following: 
Prompt the user to enter a factorial starting integer. 
  o Make sure it's valid or reprompt the user 
Call your function factorial() that:
  o takes the starting integer as its argument 
calculated the factorial using recursion 
o returns the value 
Call your function factorial2() that calculates the factorial without recursion 
Print both values with clear descriptions and formatted with thousand commas. 
'''

# while loop to validate user input
while True:
    user_number = input("Enter a positve number to calculate the factorial: ")

    # try/except block to validate user input
    try:
        user_number = int(user_number)
        # input must be a positive number
        if user_number <= 0:
            raise ValueError

    except ValueError as value_error:
        print("Please enter a valid integer...", value_error)

    else:
        break


# recursive function to calculate the factorial
def factorial(user_number):
    if user_number == 1:
        return 1
    else:
        return user_number * factorial(user_number - 1)


# regular function to calculate the factorial
def factorial2(user_number):
    result = 1
    for i in range(user_number, 0, -1):
        result *= i
    return result


# call the functions
recursion_func_result = factorial(user_number)
regular_func_result = factorial2(user_number)

# format the result
formatted_message = f'a recursion function: {recursion_func_result:,}'
dash_number = len(formatted_message)

print(f"\nThe result of a {user_number}! factorial using... ")
print('-' * dash_number)
print(formatted_message)
print('-' * dash_number)
print(f"a regular function: {regular_func_result:,}")
