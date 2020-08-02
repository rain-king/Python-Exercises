#!/bin/python

def first(st):
    chars = []
    repeated = []
    for i in range(len(st)):
        char = st[i]
        if not char in chars: #store one of each char into chars
            chars.append(char)
        else: #if char is repeated, add into repeated
            repeated.append(char)
    for i in range(len(st)):
        char = st[i]
        if not char in repeated: #exit returning the first char not in repeated
            return i+1 #1-indexed
    return 0

print(first(input()))
