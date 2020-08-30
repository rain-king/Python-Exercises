#!/bin/python

# Given an integer n, create a two-dimensional array of size (n×n) and populate it as follows, with spaces between each character:

#    The positions on the minor diagonal (from the upper right to the lower left corner) receive 1 .
#    The positions above this diagonal recieve 0 .
#    The positions below the diagonal receive 2 . 

# Print the elements of the resulting array. 

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
