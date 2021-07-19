#Euler Problem 23
'''
A perfect number is a number for which the sum of its proper divisors is exactly 
equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and 
it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of 
two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is 
known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this 
limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import math 

def Divisors(x):
    divisors = []
    for i in range(1,int(math.sqrt(x))+1):
        if x % i == 0:
            divisors.append(i)
            if i != int(x/i):
                divisors.append(int(x/i))
    divisors.remove(x)
    return sorted(divisors)

def AbundantNumbers():
    limit = 28123
    abundant = []
    for j in range(1,limit+1):
        if j < sum(Divisors(j)):
            abundant.append(j)
    return abundant

def Compute():
    limit = 28123
    allnumberslessthan28124 = [x for x in range(1,limit+1)]
    abundantsumnumbers = []
    abundantnumbers = AbundantNumbers()
    for i in range(12, limit + 1):
        for j in range(len(abundantnumbers)):
                if (i - abundantnumbers[j]) in abundantnumbers:
                    abundantsumnumbers.append(i)
                    break
                elif i < abundantnumbers[j]:
                    break
    requiredsum = sum(allnumberslessthan28124) - sum(abundantsumnumbers)
    return requiredsum

print(Compute())
    