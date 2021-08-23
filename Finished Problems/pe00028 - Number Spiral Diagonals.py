'''

Project Euler Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 
spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Answer:
    669171001
--- 0.0004291534423828125 seconds ---
'''
import time
    
def compute(x):
    totalsum = 1
    for i in range(3,x+1,2):
        totalsum += 4*i**2 - 6*(i-1)
    return totalsum

if __name__ == "__main__":
    start_time = time.time()
    print(compute(1001))
    print("--- %s seconds ---" % (time.time() - start_time))