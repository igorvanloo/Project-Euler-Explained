#Project Euler Problem 21

#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b 
#are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
#The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.

import math

def Divisors(x):
    divisors = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(int(x/i))
    divisors.remove(x)
    return sorted(set(divisors))

def sumofdivisor(x):
    testlist = Divisors(x)
    total = sum(testlist)
    return total

def Compute():
    amicablenum = []
    for i in range(1,1000001):
        if i == sumofdivisor(sumofdivisor(i)):
            if i == sumofdivisor(i):
                pass
            else:
                amicablenum.append(i)
    print(amicablenum)
    return sum(amicablenum)

print(Compute())
                   