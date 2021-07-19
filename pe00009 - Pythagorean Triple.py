'''
Project Euler Problem 9 

Anwser:
    
'''

import time, math, eulerlib

def ppt(limit):
    for m in range(2,int(math.sqrt(1000))+1):
        for n in range(1,m):
            if (m+n) % 2 == 1 and math.gcd(m,n) == 1:
                a = m**2 + n**2
                b = m**2 - n**2
                c = 2*m*n
                
                p = a+b+c
                
                for k in range(1,int(limit/p)+1):
                    if k*p == limit:
                        return k**3*a*b*c
                        break

if __name__ == "__main__":
    start_time = time.time()
    print(ppt(1000))
    print("--- %s seconds ---" % (time.time() - start_time))
            
            