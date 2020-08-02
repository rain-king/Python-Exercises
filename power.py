#!/bin/python
def power(a,n):
    if n == 0:
        pow = a
    else:
        pow = a*power(a,n-1)
    return pow

print(power(float(input()),int(input())))
