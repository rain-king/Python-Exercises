#!/bin/python
def getkey(word,dictionary):
    for key in dictionary:
        if word == dictionary[key]:
            return key
        if word == key:
            return dictionary[key]
    return -1

def getdict(n):
    dictionary = dict()
    for i in range(n):
        words = input().split()
        dictionary[words[0]] = words[1]
    return dictionary

synonims = getdict(int(input()))
print(getkey(input(),synonims))
