a = [1, 2, 3, 4]
b = [1, 2, 3, 5]
# works one by one, index by index

print(a < b)
print(a > b)
print(a == b)
print(a != b)
print(a <= b)
print(sum(a))
print(min(a))
print(max(a))
print('-' * 20)
for value in a:
    print(value + b[2], end="\n")

a[0] = True
a[:2] = 'cool'
print(a)
a.extend(b)
a.reverse()
print(a)


def my_func(str_arg):
    convert_to_list = list(str_arg)
    print('list: ', convert_to_list)
    convert_to_list.sort()
    print('sorted: ', convert_to_list)
    join_again = ''.join(convert_to_list)
    print('join again, but sorted: ', join_again)
    return join_again


print(my_func('pedro'))


print(''.join(sorted([x for x in 'la soledad'])))
