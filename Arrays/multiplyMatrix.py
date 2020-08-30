#!/bin/python

# Given three positive integers m, n and r, m lines of n elements, giving an m×n matrix A, and n lines of r elements, giving an n×r matrix B, form the product matrix AB, which is the m×r matrix whose (i,k) entry is the sum
# A[i][1]∗B[1][k]+⋯+A[i][n]∗B[n][k]
# and print the result. 

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
