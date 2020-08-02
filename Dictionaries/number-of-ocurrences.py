#!/bin/python
x = [str(i) for i in input().split()]
dic = dict()
out = []
for i in x:
    if i not in dic:
        dic[i] = 0
    else:
        dic[i] += 1
    out.append(dic[i])
print(*out)

