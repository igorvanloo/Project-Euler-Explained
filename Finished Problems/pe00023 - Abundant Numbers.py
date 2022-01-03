'''
Project Euler Problem 23

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

Anwser:
    4179871
--- 3.437476873397827 seconds ---
'''

import math , time

def Divisors(x):
    divisors = []
    for i in range(1,int(math.sqrt(x))+1):
        if x % i == 0:
            divisors.append(i)
            if i != int(x/i):
                divisors.append(int(x/i))
    divisors.remove(x)
    return sum(set(divisors))

def compute():
    abundantnums = []
    for x in range(1,28123 + 1):
        if x < Divisors(x):
            abundantnums.append(x)
        
    array = [True]*28124
    for y in range(len(abundantnums)):
        for z in range(y, len(abundantnums)):
            if abundantnums[y]+abundantnums[z] < 28124:
                array[abundantnums[y]+abundantnums[z]] = False
    return sum([i for i in range(len(array)) if array[i]])

if __name__ == "__main__":
    start_time = time.time()
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
    