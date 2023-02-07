'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/6/2023
Homework Problem # 3_5
Description:
write a python program that performs the following steps: 
Open and read the file created above line by line,
each line contains the name, id, and gpa of a student,
parse the data in each row (records of one student) into a 3 element tuple, 
store each tuple in a single list and print the list of tuples to the console 
when the file is fully processed
'''

import os

absolute_path = os.path.dirname(__file__)
relative_path = "cs521_3_5_input.txt"
# open the file
input_file = open(os.path.join(absolute_path, relative_path), 'r')
students_records = []

for line in input_file:
    line = line.split(',')
    # remove the trailing
    name, id, gpa = line[0].strip(), line[1].strip(), line[2].strip()
    # append the tuple to the list
    students_records.append((name.replace('\xa0', ' '), id, gpa))

print()
print("Student Records:", students_records)

input_file.close()
