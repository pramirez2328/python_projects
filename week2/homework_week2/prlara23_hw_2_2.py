'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 01/26/2023
Homework Problem # 2_2
Description:
print input 3 times as a string, integer and float
'''

user_input = input("Enter a string or a number: ")

# prints the input as a string 3 times
print('user\'s input as a string 3 times: ', user_input * 3)

# prints the input as an integer 3 times
print('user\'s input as an integer 3 times: ', int(user_input * 3))

# prints the input as a float 3 times
print('user\'s input as a float 3 times: ', float(user_input * 3))

'''
if the user enters a numerical value like '7', the program will not crash,
because the input can be converted to an integer or float.
But, if the user enters a letter, word, or any other character,
the program will crash! because the input cannot be converted
into an integer or float.
To solve this problem, we can check if the input isnumeric(),
by creating a conditional statement that checks if the value can be converted.
if the value is not numerical then the program can skip
the last two prints(conversions).
'''
