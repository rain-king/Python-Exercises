#!/bin/python
def reverse(x):
    if len(x) <= 1:
        y = x
    else:
        y = [x[-1]]+reverse(x[:-1])
    return y

def main():
    x = []
    while not 0 in x:
        x.append(int(input()))
    x = reverse(x)
    for i in range(0,len(x)):
        print(x[i])

main()
