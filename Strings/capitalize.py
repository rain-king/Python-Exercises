#!/bin/python
def capitalize(words):
    x = words.split()
    for word in range(0,len(x)):
        ascii = ord(x[word][0])
        if ascii in range(97,123):
            x[word] = chr(ascii-32)+x[word][1:]
    return x

print(*capitalize(input()))
