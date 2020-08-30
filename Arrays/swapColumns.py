#!/bin/python

# Given two positive integers m and n, m lines of n elements, giving an m×n matrix A, followed by two non-negative integers i and j less than n, swap columns i and j of A and print the result.

# Write a function swap_columns(a, i, j) and call it to exchange the columns. 

def swap_rows(A,m,n):
    save = A[m]
    A[m] = A[n]
    A[n] = save
    return A

def swap_columns(A,m,n):
    rowsNumber = len(A)
    for i in range(rowsNumber):
        save = A[i][m]
        A[i][m] = A[i][n]
        A[i][n] = save
    return A

if __name__ == '__main__':
    m,n = [int(i) for i in input().split()]
    A = [[int(j) for j in input().split()] for i in range(m)]
    i,j = [int(i) for i in input().split()]
    A = swap_columns(A,i,j)
    print(*[A[i] for i in range(m)])
