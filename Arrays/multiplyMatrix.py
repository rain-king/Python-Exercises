#!/bin/python

def multiply(A,B):
    m,n,r = len(A),len(B),len(B[0])
    C = [[0]*r for i in range(m)]
    for i in range(m):
        for j in range(r):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
    return C

if __name__ == '__main__':
    m, n, r = [int(i) for i in input().split()]
    A = [[int(j) for j in input().split()] for i in range(m)]
    B = [[int(j) for j in input().split()] for i in range(n)]
    A = multiply(A,B)
    for i in range(m):
        print(*A[i])
