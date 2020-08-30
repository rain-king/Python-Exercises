#!/bin/python

# Given two integers representing the rows and columns (m×n), and subsequent m rows of n elements, find the index position of the maximum element and print two numbers representing the index (i×j) or the row number and the column number. If there exist multiple such elements in different rows, print the one with smaller row number. If there multiple such elements occur on the same row, output the smallest column number.

def maximum(A):
    m,n = len(A),len(A[0])
    max = [0,0]
    for i in range(m):
        for j in range(n-1):
            if A[i][j+1] > A[max[0]][max[1]]:
                max = [i,j+1]
        if A[i][0] > A[max[0]][max[1]]:
            max = [i,0]
    return max

if __name__ == '__main__':
    m,n = [int(i) for i in input().split()]
    A = [[int(j) for j in input().split()] for i in range(m)]
    print(*maximum(A))
