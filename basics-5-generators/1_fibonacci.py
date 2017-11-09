"""SERIES  0,1,1,2,3,5,8,13,21,34,55,89..."""

def fib()
    a, b = 0,1
    yield a
    while  True:
        yield b
        a,b = b, a+b

n = int(input("Enter Length : "))
for _ in range(n)
    print fib()
