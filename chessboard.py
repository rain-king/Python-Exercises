#!/bin/python
def chessboard(m,n):
    A = [[] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if (i+j)%2:
                s = '*'
            else:
                s = '.'
            A[i].append(s)
    return A

m,n = [int(i) for i in input().split()]
A = chessboard(m,n)
for i in range(m):
    print(*A[i])
