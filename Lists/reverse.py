#!/bin/python

def reverse(x):
    y = []
    n = len(x)
    for i in range(0,n):
        y.append(x[n-i-1])
    return y

if __name__ == '__main__':
    x = []
    while 0 not in x:
        x.append(int(input()))
    for k in range(0,len(x)):
        print(reverse(x)[k])
