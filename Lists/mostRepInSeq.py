#!/bin/python

# way easier with dictionaries
def listAndMostRepetitions(lst):
    lastIndex = 0
    repetitions, moreRepetitions = 1, 1
    noRepeatedLst = list()
    for i in range(1, lst.__len__()):
        if lst[i-1] == lst[i]:
            repetitions += 1
            if repetitions > moreRepetitions:
                moreRepetitions = repetitions
        else:
            noRepeatedLst.append((lastIndex, repetitions))
            repetitions = 1
            lastIndex = i
    noRepeatedLst.append((lastIndex, repetitions))
    return noRepeatedLst, moreRepetitions

def mostRepInSeq(lst):
    noRepeatedLst, mostRepetitions = listAndMostRepetitions(lst)
    for indexRepetitions in noRepeatedLst:
        if indexRepetitions[1] == mostRepetitions:
            return indexRepetitions

lst = list() 
x = None
while x != '0':
    x = input()
    lst.append(x)
print(mostRepInSeq(lst))