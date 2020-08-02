#!/bin/python
dic = dict()
for i in range(int(input())):
    st = input().split()
    if st[0] not in dic:
        dic[st[0]] = int(st[1])
    else:
        dic[st[0]] += int(st[1])
for i in sorted(dic.keys()):
    print(i, dic[i])
