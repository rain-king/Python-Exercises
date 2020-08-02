#!/bin/python
def snowflake(n):
    A = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or n-i-1 == j or i == (n+1)/2-1 or j == (n+1)/2-1:
                A[i].append('*')
            else:
                A[i].append('.')
    return A

n = int(input())
A = snowflake(n)
for i in range(n):
    print(*A[i])
