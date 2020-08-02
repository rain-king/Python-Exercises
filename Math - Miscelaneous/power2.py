#!/bin/python
def power(a,n):
    pow = 1
    for i in range(0,abs(n)):
        pow = pow*a
    if n < 0:
        pow = 1/pow
    return pow

print(power(float(input()),int(input())))
