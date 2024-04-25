# exercise 1
def nested_sum(l: list):
    total = 0
    for e in l:
        total += sum(e)
    return total

def test_exercise1():
    assert nested_sum([[1, 2], [3], [4, 5, 6]]) == 21

# exercise 2
def cumsum(l: list):
    sublists = [l[:i] for i in range(1, len(l)+1)]
    return [sum(x) for x in sublists]

def test_exercise2():
    assert cumsum([1, 2, 3]) == [1, 3, 6]

# exercise 3
def middle(l: list):
    return l[1:len(l)-1]

def test_exercise3():
    assert middle([1,2,3,4]) == [2,3]

# exercise 4
def chop(l: list):
    del l[0]
    del l[len(l)-1]
    return None

def test1_exercise4():
    t = [1,2,3,4]
    assert chop(t) == None

def test2_exercise4():
    t = [1,2,3,4]
    chop(t)
    assert t == [2,3]

# exercise 5
def is_sorted(l: list):
    return l == sorted(l)

def test1_exercise5():
    assert is_sorted([1,2,2])

def test2_exercise5():
    assert not is_sorted(['b', 'a'])

# exercise 6
def is_anagram(str1: str, str2: str):
    return set(str1.lower()) == set(str2.lower())

def test1_exercise6():
    assert is_anagram('pot', 'Top')

def test2_exercise6():
    assert not is_anagram('foo', 'bar')

# exercise 7
def has_duplicates(l: list):
    return len(set(l)) != len(l)

def test1_exercise7():
    assert has_duplicates([1,1,2])

def test2_exercise7():
    assert not has_duplicates([1,2,3])

# exercise 8
from random import randint
def experiment():
    l = [randint(1,365) for i in range(23)]
    return has_duplicates(l)

from statistics import mean
print(mean([experiment() for i in range(10000)]))
