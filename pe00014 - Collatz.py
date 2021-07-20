'''
Project Euler Problem 14

Collatz Sequence
n → n/2 (n is even)
n → 3n + 1 (n is odd)


Anwser:
    837799
--- 14.294111013412476 seconds ---
    
'''

import time, math

def Collatz(n):
    count = 1
    while n != 1:
        if n % 2 ==0:
            n = n/2
            count += 1
        else:
            n = (3*n +1)/2
            count += 2
    return count

def compute(limit):
    array = [0]*(limit+1)
    for x in range(1,limit+1):
        array[x] = Collatz(x)
    return array.index(max(array))

if __name__ == "__main__":
    start_time = time.time()
    print(compute(10**2))
    print("--- %s seconds ---" % (time.time() - start_time))






    

    