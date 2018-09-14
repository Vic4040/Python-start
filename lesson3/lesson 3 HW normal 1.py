
try:
    n = int(input('please enter fibonacci array member M here: '))
    m = int(input('please enter fibonacci array member N here: '))
except ValueErroe:
    print("input numbers only")
    exit(1)
def fibonacci(n, m):

    a = 0
    b = 1
    c = [a, b]
    while a < 1000:
        i = (a + b)
        a = b
        b = i
        c.append(i)
    return print(с)

