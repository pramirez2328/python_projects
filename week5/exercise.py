arg = 5
arg2_list = [1, 2, 3, 4, 5]


def my_func(arg, arg2_list):
    arg += 1
    arg2_list[0] = arg
    print('arg inside', arg, id(arg))
    print('arg2 inside', arg2_list, id(arg2_list))
    return arg, arg2_list


print(my_func(arg, arg2_list))
print(arg, id(arg))
print(arg2_list, id(arg2_list))

# print(__name__ == '__main__')


# var = 'hello  world'
# var1 = 0
# var2 = 1

# try:
#     print(var.split())
# except ValueError:
#     print('this is a value error')
# except TypeError:
#     print('this is a type error')
# except ZeroDivisionError:
#     print('Division by zero')
# except Exception:
#     print('Something went wrong')
# else:
#     print('No errors')
# finally:
#     print('This will always run')

# print(dir(locals()['__builtins__']))



