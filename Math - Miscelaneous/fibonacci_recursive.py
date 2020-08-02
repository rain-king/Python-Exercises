#!/bin/python
def fib(n):
    if n == 0:
        f = 0
    elif n == 1:
        f = 1
    else:
        f = fib(n-1)+fib(n-2)
    return f

print(fib(int(input())))
