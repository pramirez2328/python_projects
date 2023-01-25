first = int(input("Enter a number: "))
second = int(input("Enter another number: "))

teens = 0
loop_count = 0

while first > 10 and second < 20:
    if first == 10 or second == 20:
        teens += 1
    first -= 5
    second += 5
    loop_count += 1


print('first', first)
print('second', second)
print('teens', teens)
print('loop', loop_count)
