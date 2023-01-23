t = input(
    "Do you want to convert from Celsius"
    + "to Fahrenheit or"
    + "from Fahrenheit to Celsius? (C/F): "
)

t = t.upper()

while t != "C" and t != "F":
    t = input("Please enter C or F: ")

if t == "C":
    c = input("    Enter the temperature in Celsius: ")
    if c.isnumeric():
        f = int(int(c) * 9 / 5 + 32)
        print("    The temperature in Fahrenheit is:", f)
    else:
        print("    The temperature must be a number")
else:
    f = input("    Enter the temperature in Fahrenheit: ")
    if f.isnumeric():
        c = int((int(f) - 32) * 5 / 9)
        print("    The temperature in Celsius is:", c)
    else:
        print("    The temperature must be a number")
