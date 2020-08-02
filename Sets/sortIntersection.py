#!/bin/python
print(*sorted(set(input().split()) & set(input().split())))
