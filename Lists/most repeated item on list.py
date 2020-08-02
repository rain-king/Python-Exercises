#!/bin/python
def maxreplen(list):
    i = 0
    counter = [1,1]
    status = False
    while i+1 < len(list):
        if list[i] == list[i+1]:
            counter[0] += 1
        else:
            if counter[0] > counter[1]:
                counter[1] = counter[0]
            counter[0] = 1
        i += 1
    return counter[1]

list = []
x = ''
while x != '0':
    x = input()
    list.append(x)
print(maxreplen(list))
