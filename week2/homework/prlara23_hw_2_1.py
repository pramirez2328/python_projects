'''
Pedro Ramirez
homework 2.1
CS-521
write a program that asks the user to enter a whole number from 1 to 7.
'''

whole_num = int(input("Enter a whole number from 1 to 7: "))

result = whole_num * 2 + 10 // 2 - whole_num
# prints the result from previous line
print()
print("-- The result of the first calculation is", result, '\n')

first_digit = int(whole_num)
second_digit = first_digit + 1
third_digit = first_digit + 2
three_digit_num = int(str(first_digit) + str(second_digit) + str(third_digit))
sum = first_digit + second_digit + third_digit

# prints the sum of the digits in the three digit number
print("-- The sum of the three_digit_number variable is", sum, '\n')

result2 = three_digit_num / sum
# prints the result as a float
print("-- The division result as a type of float is", result2, '\n')

# prints the result as an integer
print(f'-- The truncated result as a type of integer is {int(result2)}')
