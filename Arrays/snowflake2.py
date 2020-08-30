#!/bin/python

# Given an odd number integer n, produce a two-dimensional array of size (n×n). Fill each element with a single character string of "." . Then fill the middle row, the middle column and the diagnals with the single character string of "*" (an image of a snow flake). Print the array elements in (n×n) rows and columns and separate the characters with a single space. 

def snowflake(n):
    A = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or n-i-1 == j or i == (n+1)/2-1 or j == (n+1)/2-1:
                A[i].append('*')
            else:
                A[i].append('.')
    return A

if __name__ == '__main__':
    n = int(input())
    A = snowflake(n)
    for i in range(n):
        print(*A[i])
