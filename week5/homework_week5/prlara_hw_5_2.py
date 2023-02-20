'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/19/2023
Homework Problem # 5_2
Description:
Create 3 functions with docstring:
1. letter_counts() takes a string as its argument and
   returns a dictionary of the letters as keys and frequency counts as values.
2. most_common_letter() takes a string as its argument
   and returns a list of the most common letter(s).
   This function should call letter_counts().
3. string_count_histogram() takes a string as its argument
   and returns a list of the unique letters,  with each letter
   being the repeated number of times it appears in the string.
   This list will then be printed one element per line (as a histogram).
   This function should call letter_counts().
'''


def letter_counts(sentence):
    '''Takes a string as its argument and returns a dictionary of the letters
    as keys and frequency counts as values.
    '''
    letter_dict = {}
    remove_whitespace = sentence.replace(" ", "")
    for char in remove_whitespace:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1

    return letter_dict


def most_common_letter(sentence):
    '''Takes a string as its argument and returns a list of the most common
    letter(s).
    '''
    letter_dict = letter_counts(sentence)
    most_common = []
    max_value = max(letter_dict.values())
    for key, value in letter_dict.items():
        if value == max_value:
            most_common.append(key)

    return most_common


def string_count_histogram(sentence):
    '''Takes a string as its argument and returns a list of the unique
    letters,  with each letter being the repeated number of times it appears
    in the string.
    '''
    letter_dict = letter_counts(sentence)
    histogram = []
    for key, value in letter_dict.items():
        histogram.append(key * value)

    return histogram


# Assign a sentence of at least 15 characters into a constant string variable.
str_analyzed = "WWWAS IT A RAT I SAW"

if __name__ == '__main__':
    print("The string being analyzed is: " + str_analyzed)

    # call letter_counts() function and sort alphabetically
    dict_sorted = dict(sorted(letter_counts(str_analyzed).items()))

    # create a string from the dictionary and remove the curly braces
    letter_counts_str = str(dict_sorted).replace("{", "").replace("}", "")

    print(f'1. Letter counts: {letter_counts_str}')

    # -----------------------------------------------------------------------

    # call most_common_letter() function and sort alphabetically
    common_letters = sorted(most_common_letter(str_analyzed))

    # collect the number of times the most common letter appears
    times = dict_sorted[common_letters[0]]

    # condition to handle the grammar of the output
    last_message = ''
    if len(common_letters) == 1:
        last_message = f'appears {times} times'
    else:
        last_message = f'each appear {times} times.'

    # create a string from the list and remove the brackets
    common_letters = str(common_letters)
    common_letters = common_letters.replace("[", "").replace("]", "")

    print(f'2. Most frequent letter {common_letters} {last_message}')

    # --------------------------------------------------------------------------

    # call string_count_histogram() function and sort alphabetically
    histogram = sorted(string_count_histogram(str_analyzed))
    print('3. Histogram:')

    # print the histogram one element per line
    for item in histogram:
        print(f'   {item}')
