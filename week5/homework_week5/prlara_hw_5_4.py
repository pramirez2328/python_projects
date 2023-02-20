'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/19/2023
Homework Problem # 5_4
Description:
Write a python program that does the following:
Prompt for a file name of text words. 
Words can be on many lines with multiple words per line.
Read the file, remove all punctuation 
(leaving just a space between words),and convert the words to a list. 
Call a function you created called list_to_twice_words()
that takes a list as an argument and returns a list 
that contains only words that occurred exactly TWICE in the file.
Print the results of the function with an appropriate description.
'''
import os
import string

# creates the path to the file
external_file = 'words.txt'
path = os.path.join(os.path.dirname(__file__), external_file)

# opens the file
words_file = open(path, 'r')

words_list = []

# removes punctuation and converts the words to a list
for line in words_file:
    for char in line:
        if char in string.punctuation:
            line = line.replace(char, '')
    line_split = line.split()
    words_list.extend(line_split)


# creates a function that takes a list as an argument
def list_to_twice_words(words_list):
    '''Returns a list that contains only words
    that occurred exactly TWICE in the file
    '''
    words_dict = {}
    for word in words_list:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return [word for word in words_dict if words_dict[word] == 2]


twice_words_list = list_to_twice_words(words_list)

# formats the output depending on the number of words
result = 'Those words are:' if len(twice_words_list) > 1 else 'This word is:'
s_file = 's' if len(words_list) != 1 else ''
s_list = 's' if len(twice_words_list) != 1 else ''


# prints the results
print()
print(f'The file {external_file} contains {len(words_list):,} word{s_file}.')
print(
    f'Within this file, there are {len(twice_words_list):,} \
word{s_list} that occurred exactly twice in the file'
)
if len(twice_words_list) > 0:
    print(f'{result}\n{twice_words_list}')

words_file.close()
