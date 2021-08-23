'''
Project Euler Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions 
with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

Reasoning

The basis of this proof is that all nonprimes intergers can be made as a product of other integers
Similarly the recurring decimals will be the same for example 1/126 = 1/7 * 1/6 * 1/3 recurring decimal is still 6
Therefore we will look for the recurring decimals of all the primes numbers

From fermats little theorem the recurring decimal length is equal to the order of 10 modulo p
This means that 10^x congruent to 1 mod p, x is our recurring decimal length
So we iterature from x: 1 till p-1, on 10^x once 10^x mod p = 1 we stop and return that length

Lastly we create a dictionary so that we can add which prime corresponds to which length
We return the key (In this case the prime) which corresponds to the maximum length value 

Answer:
    
'''
import time, math

def list_primality(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(int(math.sqrt(n)) + 1):
		if result[i]:
			for j in range(2 * i, len(result), i):
				result[j] = False
	return result

def list_primes(n):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

def lengthofdecimal(x): 
    for i in range(1,x):
        if (10**i) % x == 1:
            return i
            break

def compute(limit):
    allprimes = [3] + list_primes(limit)[3:]
    array = [0]*(limit + 1)
    for i in range(len(allprimes)):
        length = lengthofdecimal(allprimes[i])
        array[allprimes[i]] = length
    return array.index(max(array))

if __name__ == "__main__":
    start_time = time.time()
    print(compute(1000))
    print("--- %s seconds ---" % (time.time() - start_time))
        

