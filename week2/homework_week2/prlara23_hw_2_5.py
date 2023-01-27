'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 01/26/2023
Homework Problem # 2_5
Description:
prints foo If the number is divisible by 2, 
print bar if the number is divisible by 3,
print the word baz if the number is divisible by 5,
print the combination on the same line if the number is
divisible by two or more of these numbers.  
If the number is not divisible by 2,3 or 5, do not print a string.
Also, print a line of 30 dashes.
'''

MAXVAL = 30

for i in range(1, MAXVAL + 1):
    # prints foobarbaz if the number is divisible by 2, 3 and 5
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        print(f'{i}: foobarbaz')
    # prints foobar if the number is divisible by 2 and 3
    elif i % 2 == 0 and i % 3 == 0:
        print(f'{i}: foobar')
    # prints foobaz if the number is divisible by 2 and 5
    elif i % 2 == 0 and i % 5 == 0:
        print(f'{i}: foobaz')
    # prints barbaz if the number is divisible by 3 and 5
    elif i % 3 == 0 and i % 5 == 0:
        print(f'{i}: barbaz')
    elif i % 2 == 0:
        print(f'{i}: foo')
    elif i % 3 == 0:
        print(f'{i}: bar')
    elif i % 5 == 0:
        print(f'{i}: baz')
    else:
        print(f'{i}: ')

print('------------------------------')

# prints a line of 30 dashes to mimic previous print
i = 1
while i <= MAXVAL:
    print('-', end='')
    i += 1
