'''
Project Euler Problem 

Project Euler 20
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!

math.factorial() #This is predefined factorial function 

Anwser:
    648
--- 0.00012803077697753906 seconds ---
'''

import time, math

def sum_digits(x):
    totalsum = 0
    while x != 0:
        totalsum += x % 10
        x = x // 10
    return totalsum

def factorial(x): #Self created
    fact = 1
    for i in range(1, x+1):
        fact = fact * i
    return fact

if __name__ == "__main__":
    start_time = time.time()
    print(sum_digits(math.factorial(100)))
    print("--- %s seconds ---" % (time.time() - start_time))
    