#!/bin/python
def matrix(n):
    A = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j+k or i == j-k:
                    A[i].append(k)
    return A

n = int(input())
A = matrix(n)
for i in range(n):
    print(*A[i])
