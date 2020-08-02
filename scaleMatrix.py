#!/bin/python
def scale(A,c):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = c*A[i][j]
    return A

m, n = [int(i) for i in input().split()]
A = [[int(j) for j in input().split()] for i in range(m)]
c = int(input())
A = scale(A,c)
for i in range(m):
    print(*A[i])
        
