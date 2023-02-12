'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/12/2023
Homework Problem # 4_2
Description:
Write the following python program.
a. Assign a SENTENCE of at least 15 characters into a string constant
b. Perform analysis that counts the number of each letter in the string
c. Write print statements with appropriate descriptions
'''


SENTENCE = 'wwas it a rat I saw?'

obj = dict()

for char in SENTENCE:
    # storageev every letter in the string and count how many times it appears
    if char.isalpha():
        obj[char.upper()] = obj.get(char.upper(), 0) + 1

# Sort the dictionary by key and get the most frequent letter
sorted_obj = {k: v for k, v in sorted(obj.items(), key=lambda x: x[0])}
most_freq = [k for k, v in obj.items() if v == max(sorted_obj.values())]

# If there is more than one most frequent letter, add an 's' to letter
s = '' if len(most_freq) == 1 else 's'

print('The string being analyzed is: "{}"'.format(SENTENCE))
print('1. Dictionary of letter counts: {}'.format(sorted_obj))
print('2. Most frequent letter{} {}'.format(s, most_freq))
