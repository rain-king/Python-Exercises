#!/bin/python
fnum = []
def fib(n):
    for i in range(0,n):
        if i+1 <= len(fnum):
            f = fnum[i]
        if i <= 1:
            f = 1
        else:
            f = fnum[i-1]+fnum[i-2]
        fnum.append(f)
    return fnum

print(fib(int(input())))
