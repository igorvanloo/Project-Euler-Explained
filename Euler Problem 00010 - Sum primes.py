#Project Euler Problem 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
import eulerlib

def bettersumprime():
    requiredprime = 2000000
    return sum(eulerlib.primes(requiredprime))

def prime(z):
    primes = [2]
    for x in range(3,z,2):
        for y in range(2,x):
            if x % y == 0:
                break
        else:
            primes.append(x)
    return primes

def sumprime():
    requiredprime = 2000000
    return sum(prime(requiredprime))

