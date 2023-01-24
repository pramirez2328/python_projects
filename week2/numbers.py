# base 8
print(0o10 + 2)

# base 16
print(0x10 + 2)

# base 2
print(0b10 + 2)


# string attributes

print('upper', "Hello World".upper())
print('lower', "Hello World".lower())
print('capitalize', "Hello World".capitalize())
print('title', "Hello World".title())
print('swapcase', "Hello World".swapcase())
print('casefold', "Hello World".casefold())
print('count', "Hello World".count("l"))
print('count with one number', "Hello World".count("l", 3))
print('count with two numbers', "Hello World".count("l", 3, 7))
print('endswith d', "Hello World".endswith("d"))
print('ends with d and arguments', "Hello World".endswith("d", 0, 5))
print('ends with d and arguments II', "Hello World".endswith("d", 0, 11))
print('starts with h', "hello World".startswith("H"))

print(30 - 3**2 + 8 // 3**2 * 10)
