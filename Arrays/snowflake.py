#!/bin/python

def snowflake(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if i == j or n-i-1 == j or i == (n+1)/2-1 or j == (n+1)/2-1:
                A[i][j] = '*'
            else:
                A[i][j] = '.'
    return A

n = int(input())
if not n%2:
    n += 1
A = [[0]*n for i in range(n)]
A = snowflake(A)
for i in range(n):
    print(*A[i])
