#!/bin/python
N,M = set(),set()
n, m = input().split()
n, m = int(n), int(m)
for i in range(0,n):
    N = N | {int(input())}
for i in range(0,m):
    M = M | {int(input())}

def print_set(A):
    A = sorted(A)
    print(len(A))
    for i in A:
        print(i)

for i in [N & M, N - M, M - N]:
    print_set(i)
