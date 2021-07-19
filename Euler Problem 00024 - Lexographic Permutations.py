#Project Euler problem 24
'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible 
permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or 
alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import itertools

numbers = [x for x in range(0,10)]

def lexicographic():
    comb = []
    for L in range(10, len(numbers)+1):
        for subset in itertools.permutations(numbers, L):
            comb.append(subset)
    requiredcomb = comb[999999]
    requirednum = ""
    for i in range(0,len(requiredcomb)):
        requirednum = requirednum + str(requiredcomb[i])
    return int(requirednum)

print(lexicographic())