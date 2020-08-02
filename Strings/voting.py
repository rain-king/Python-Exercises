#!/bin/python
dic = dict()
for i in range(int(input())):
    st = [str(i) for i in input().split()]
    if st[0] not in dic:
        dic[st[0]] = 0
    else:
        dic[st[0]] += int(st[1])
