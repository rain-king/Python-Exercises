#!/bin/python
#return the number of iterations of increasing start by 10% to reach required
def days(start,required):
    total = x
    i = 1
    while total < y:
        total += 0.1*total
        i += 1
    return i

print(days(int(input()),int(input())))
