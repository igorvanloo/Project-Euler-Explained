'''
Project Euler Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b 
are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.

Anwser:
    [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368]
    31626
--- 0.0870058536529541 seconds ---
    
'''

import math,time

def Divisors(x):
    divisors = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(int(x/i))
    divisors.remove(x)
    return sum(list(set(divisors)))

def compute():
    amicablenum = []
    for i in range(1,10001):
        if i == Divisors(Divisors(i)):
            if i == Divisors(i):
                pass
            else:
                amicablenum.append(i)
    print(amicablenum)
    return sum(amicablenum)

if __name__ == "__main__":
    start_time = time.time()
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time))
                   