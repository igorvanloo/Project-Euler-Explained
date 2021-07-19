#Euler Problem 12

import math 

def totalsum(y):
    totalsum1 = int((sum(x for x in range(1,y+1))))
    return int(totalsum1)

def TriangleNumber(x):#This calculates the xth triangle number
    nth = (x*(x+1))/2
    return nth

def Divisors(x):
    count = 0
    end = math.sqrt(x)
    for i in range(1, int(end) + 1):
        if x % i == 0:
            count = count + 2
    return count

def Compute():
    x = 1
    while True:
        if Divisors(TriangleNumber(x)) >= 500:
            return TriangleNumber(x)
        else:
            print(Divisors(TriangleNumber(x)))
            x = x + 1        