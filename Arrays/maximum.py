#!/bin/python

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

def main():
    m,n = [int(i) for i in input().split()]
    A = [[int(j) for j in input().split()] for i in range(m)]
    print(*maximum(A))

main()
