#!/bin/python

# Given two positive integers m and n, m lines of n elements, giving an m×n matrix A, followed by one integer c, multiply every entry of the matrix by c and print the result. 

def scale(A,c):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = c*A[i][j]
    return A

if __name__ == '__main__':
    m, n = [int(i) for i in input().split()]
    A = [[int(j) for j in input().split()] for i in range(m)]
    c = int(input())
    A = scale(A,c)
    for i in range(m):
        print(*A[i])
            
