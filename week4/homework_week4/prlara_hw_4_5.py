'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/12/2023
Homework Problem # 4_5
Description:
Creates a constant dictionary with keys for the characters '1234567890-.'
and values that represent these characters as words.
• For the decimal point, use 'point' as the value
• For the negative sign, use 'negative' as the value
Inside of an infinite loop
• prompts a user for a number with an appropriate description
• validates that a number was entered, if valid - break out the loop
otherwise print error message and stay in loop to reprompt
convert the validated number to words and print the converted number words
'''

VALIDATION_DICT = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero',
    '.': 'point',
    '-': 'negative',
}

user_input = input('Please enter a number: ')

cond = len(user_input)
while cond > 0:
    # for loop to validate the input
    for index, char in enumerate(user_input):
        if char in VALIDATION_DICT:
            # check if the negative sign is in the middle of the number
            if char == '-' and index != 0:
                print('-- Invalid input! --')
                print('Add the negative sign at the beginning of the number.')
                break
            else:
                # if the character is valid, decrease the condition by 1
                cond -= 1
                continue
        else:
            print('-- Invalid! --')
            print('You entered invalid characters.')
            break
    # break out of the loop if the input is valid
    if cond == 0:
        break
    else:
        user_input = input('Please enter another number: ')
        cond = len(user_input)

text = ''
# convert the validated number to words
for char in user_input:
    text += VALIDATION_DICT[char] + ' '


print(f'As text: {text.strip()}')
