'''
Euler Problem 4

906609
--- 0.7705011367797852 seconds ---
'''

import time

start_time = time.time()
overall = []
def ispalindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False
    
def main():
    overall = []
    for x in range(100,1000):
        for y in range(100,1000):
            a = x*y
            test = list(str(a))
            if ispalindrome(test) == True:
                overall.append(a)
    return max(overall)

if __name__ == "__main__":
    print(main())
    print("--- %s seconds ---" % (time.time() - start_time))
    