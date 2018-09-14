try:
    n = int(input('please enter fibonacci array member N here: '))
    m = int(input('please enter fibonacci array member M here: '))
except ValueError:

    print("input numbers only")
    exit(1)


def fib(n):  # return Fibonacci series up to n
    """ряд фибоначчи по N"""
    result = []
    a, b = 1, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


f100 = fib(0x7fffffff)  # бесконечность - не предел
print(f100[n:m])  # выодим итог
