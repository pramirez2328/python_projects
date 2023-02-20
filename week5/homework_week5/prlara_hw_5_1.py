'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/19/2023
Homework Problem # 5_1
Description:
Write a python program that does the following:  
Continually prompts user for a text file to read
until a valid file is supplied. Create a function named vc_counter()
that takes the valid file name as an argument, counts the number of vowels 
and consonants in the file. Returns a dictionary of the count values,
using the keys 'vowels' and 'consonants'.
Call vc_counter() and store results to a dictionary object. 
Print the total vowels and consonants with appropriate descriptions. 
'''
import os

cond = True
print()

# Continually prompts user for a text file until a valid file is supplied
while cond:
    file_name = input("Enter a text file: ")
    try:
        path = os.path.join(os.path.dirname(__file__), file_name)
        my_file = open(path, 'r')
        cond = False
    except FileNotFoundError as error:
        print("File not found. Please try again.", error)
        continue
else:
    print("---- File found, Processing!... \n")


def vc_counter(my_file):
    '''Counts the number of vowels and consonants in the file'''
    vowels = 0
    consonants = 0
    VOWELS_STR = "AEIOU"
    CONSONANTS_STR = "BCDFGHJKLMNPQRSTVWXYZ"
    for line in my_file:
        for char in line:
            if char.upper() in VOWELS_STR:
                vowels += 1
            elif char.upper() in CONSONANTS_STR:
                consonants += 1
    return {'vowels': vowels, 'consonants': consonants}


# Call vc_counter() and store results to a dictionary object
result = vc_counter(my_file)

print(f"Total # of vowels in text file: {result['vowels']:,}")
print(f"Total # of consonants in text file: {result['consonants']:,}")

my_file.close()
