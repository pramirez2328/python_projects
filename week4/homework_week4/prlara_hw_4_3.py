'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/12/2023
Homework Problem # 4_3
Description:
Write a python program that merges two lists into a dictionary
using a zip function, If there are more last names than first names
set the missing first names to None and
print the input lists and generated dictionary
with appropriate descriptions.
'''


NAMES = ['Jane', 'John']
LAST_NAMES = ['Doe', 'Deer', 'Black']

# condition to check if the last name list is smaller than the first name list
if len(NAMES) > len(LAST_NAMES):
    print('The last name list is smaller than the first name list.')
    exit()

# set the missing first names to None
handle_no_equal_list = NAMES + [None] * (len(LAST_NAMES) - len(NAMES))
# merge the two lists into a dictionary
name_dictionary = dict(zip(LAST_NAMES, handle_no_equal_list))

print(f'First Names: {NAMES}')
print(f'Last Names: {LAST_NAMES}')
print(f'Name Dictionary: {name_dictionary}')
