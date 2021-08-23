'''
Project Euler Problem 15

Consider a string with 20 R's and 20 D's (where R, D represent right or down movement respectively), 
each string represents a path from top right to bottom left on the board, how many unique strings (and this means paths) 
can we make?
Well there are 40 letters in total and we have 20 R's and 20 D's therefore by the reasoning above there will be 
40!/(20!*20!) different ways to uniquely order the string!

Anwser:
    137846528820
--- 9.202957153320312e-05 seconds ---
'''

import time, math

def compute(n):
    return int(math.factorial(2*n)/(math.factorial(n)**2))

if __name__ == "__main__":
    start_time = time.time()
    print(compute(20))
    print("--- %s seconds ---" % (time.time() - start_time))