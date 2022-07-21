'''
Project Euler Problem 12

Anwser:
    76576500.0
--- 5.815737247467041 seconds ---
'''

import math, time

def TriangleNumber(x):#This calculates the xth triangle number
    nth = (x*(x+1))/2
    return nth

def Divisors(x): #Find the divisors of a number
    divisors = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(int(x/i))
    return len(divisors)

def compute(limit):
    x = 1
    while True:
        if Divisors(TriangleNumber(x)) >= limit:
            return TriangleNumber(x)
        x = x + 1     

if __name__ == "__main__":
    start_time = time.time()
    print(compute(500))
    print("--- %s seconds ---" % (time.time() - start_time))