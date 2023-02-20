def f(a, b, n):
    arr = [a]
    for number in range(1, n + 1):
        temp = arr[number - 1] * b
        arr.append(temp)
    return arr


init = 5
double = 2
terminate = 10
print(f(init, double, terminate))
