#!/bin/python

def matrix(n):
    A = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == n-j-1:
                x = 1
            elif i > n-j-1:
                x = 2
            else:
                x = 0
            A[i][j] = x
    return A

if __name__ == '__main__':
    n = int(input())
    A = matrix(n)
    for i in range(n):
        print(*A[i])
