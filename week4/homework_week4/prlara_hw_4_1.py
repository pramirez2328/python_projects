'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/12/2023
Homework Problem # 4_1
Description:
Write a python program to solve the following:
a. Create a constant list with the integers from 55 to 5,
but only every 10th number.
b. Generate a new list with same number of elements
as the original list such that each integer in the new list
is the sum of its nearest neighbors and itself from the original list.
c. Print both lists with descriptions.
'''
INT_LIST = list(range(55, 4, -10))

result_list = []
for i in range(len(INT_LIST)):
    # If it is the first element, add the next element
    if i == 0:
        result_list.append(INT_LIST[i] + INT_LIST[i + 1])
    # If it is the last element, add the previous element
    elif i == len(INT_LIST) - 1:
        result_list.append(INT_LIST[i] + INT_LIST[i - 1])
    # If it is not the first or last element, add the previous, next and itself
    else:
        result_list.append(INT_LIST[i] + INT_LIST[i - 1] + INT_LIST[i + 1])


print()
print('This is the original list:')
print('-' * 70)
print(f'  Original List: {INT_LIST}')
print('-' * 70)
print()
print(
    'If we add the nearest neighbors '
    + 'and itself from the original list,\n'
    + 'we get the following result:'
)
print('-' * 70)
print(f'  Result List: {result_list}')
print('-' * 70)
