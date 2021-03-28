#!/bin/python

def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)

if __name__ == __main__: reverse()