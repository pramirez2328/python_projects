'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/6/2023
Homework Problem # 3_4
Description:
Read a file located in the same directory,
validate that the file contains a single sentence of 20 words,
break up the sentence into four lines of five single spaced words,
write the lines to a new text file,
print a success message to the console with the name of the new file.
'''

import sys
import os

try:
    absolute_path = os.path.dirname(__file__)
    relative_path = "cs521_3_4_input.txt"
    # open files
    INPUT_FILE = open(os.path.join(absolute_path, relative_path), 'r')
    OUTPUT = open(os.path.join(absolute_path, "cs521_3_4_output.txt"), 'w')
    WORDS_ALLOWED = 20
    WORDS_PER_LINE = 5
    # count the number of lines in the file
    lines_per_file = open(os.path.join(absolute_path, relative_path), 'r')
    single_line = len(lines_per_file.readlines()) == 1

    for line in INPUT_FILE:
        '''
        check if the file for multiple lines
        or if the sentence has less than 20 words
        '''
        if len(line.split()) != WORDS_ALLOWED or not single_line:
            print(
                "Error: The file doesn\'t contain a 20 words "
                + "single sentence or the file has more than one line.",
                end=' ',
            )
            sys.exit()
        else:
            sentence_splited = line.split()
            count = 1
            sentence = ''
            # break the sentence into 4 lines of 5 words
            for value in sentence_splited:
                sentence += value + ' '
                if count == WORDS_PER_LINE:
                    sentence = sentence.strip()
                    print(sentence, file=OUTPUT)
                    count = 0
                    sentence = ''
                count += 1
            print(f"Success! Output written to: {relative_path}")
# if the  file doesn't exist throw an error
except IOError:
    print("Error: File does not appear to exist.")
    sys.exit()

lines_per_file.close()
INPUT_FILE.close()
OUTPUT.close()
