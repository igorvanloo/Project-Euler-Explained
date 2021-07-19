#Euler Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

def lcm(x, y):
    x = int(x)
    y = int(y)
    return (x*y)/math.gcd(x, y)

def totallcm(number):
    count = totalcount = number
    while count != 10:
        TotalLcm = lcm(count-1, totalcount)
        #print(TotalLcm)
        totalcount = TotalLcm
        count = count - 1
    print(TotalLcm)
    
totallcm(20)