#!/bin/python
import math as m
def distance(x,y):
    sum = 0
    for i in range(2):
        sum = sum + (x[i]-y[i])**2
    return m.sqrt(sum)

print(distance([float(input()),float(input())],[float(input()),float(input())]))
