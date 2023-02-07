'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/6/2023
Homework Problem # 3_2
Description:
Write a Python program does all the following steps:
Create a docstring constant with 3 sentence strings,
convert the docstring to a list with one element 
for each sentence in the docstring. 
Using a loop calculate the number of: 
uppercase letters, lowercase letters, digits, punctuation characters
and output the results from each loop in columns.
'''
import string

docString = """The rain in #Spain in 2019, rained "mainly' on the plain.
-Chicken soup is good for the soul IN 2023.
The #1 city is Chicago, -the Windy City."""

# split the docstring into a list of sentences
sentence_list = docString.split("\n")
counter = 1

print()
# print the header
print(f'#{"# Upper":>11}{"# Lower":>11}{"# Digits":>11}{"# Punct.":>11}')
# print the separator
print(f'-    {"-"*7}    {"-"*7}   {"-"*8}   {"-"*8}')
for sentence in sentence_list:
    # variables are set to 0 for each sentence
    upper, lower, digits, punct = 0, 0, 0, 0
    for char in sentence:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        elif char in string.punctuation:
            punct += 1
    # print the results
    print(f'{counter}{upper:>8}{lower:>12}{digits:>10}{punct:>11}')
    counter += 1
