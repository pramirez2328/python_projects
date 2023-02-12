'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/12/2023
Homework Problem # 4_4
Description:
write a program to:
a. calculate and print all the keys as a list.
b. calculate and print all thevalues_str
   as formatted comma separated data (not as a list).
c. print all the keys and values pairs as formatted data (not as a dictionary).
d. sort in ascending order by key and print a list of tuples
   for all the keys and values_str pairs
e. sort in ascending order by value and print as formatted data
   all the keys and value pairs
'''
MY_DICT = {'a': 15, 'c': 18, 'b': 20}

# calculate and print all the keys as a list.
keys = list(MY_DICT.keys())
print(f'Keys: {keys}')


# calculate and print all the values as formatted comma separated data.
values_str = ''
for value in MY_DICT.values():
    values_str += str(value) + ', '

values_result = values_str[:-2]
print(f'values: {values_result}')


# print all the keys and values pairs as formatted data.
key_value_pairs = ''
print('Key value pairs: ', end='')
for key, value in MY_DICT.items():
    key_value_pairs += f'{key}: {value}, '

key_value_pairs_result = key_value_pairs[:-2]
print(key_value_pairs_result)


# sort in ascending order by key and print a list of tuples
sorted_keys = sorted(MY_DICT.items(), key=lambda x: x[0])
print(f'Key value pairs ordered by key: {sorted_keys}')


# sort in ascending order by value and print as formatted data
sorted_values = sorted(MY_DICT.items(), key=lambda x: x[1])
strip_brackets = str(sorted_values).strip("[]")
sorted_str = strip_brackets.replace("(", "").replace(")", "").replace("'", "")
print(f'Key value pairs ordered by value: {sorted_str}')
