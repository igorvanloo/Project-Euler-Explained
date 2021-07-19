#Euler Problem 7 - Way too slow

import eulerlib

def isprime(x):
    for y in range(2,x+1,2):
        if x % y == 0:
            print("Not prime")
            break
        else:
            print("Is prime")
            
def prime(z):
    primes = [2]
    for x in range(3,z,2):
        for y in range(2,x):
            if x % y == 0:
                break
        else:
            primes.append(x)
    return primes

def numberofprimes(length):
    return len(prime(length))
    
while True:
    num = 104742
    if numberofprimes(num) == 10000:
        print(num)
        break
    else:
        num = num + 1
        
eulerlib.prime_gen(10001)