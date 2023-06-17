# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:23:50 2023

@author: igorvanloo
"""
'''
Project Euler Problem 443

if gcd(n, g(n - 1)) = 1 then g(n) = g(n - 1) + 1

I notice that we start at 4 stop at 8 jump at 9, stop 16 jump

Testing to see the difference between jumps
x | is_prime | amount till jump | decomposition
6 | False | 2 |
9 | False | 3 |
17 | True | 8 | (17=9*2-1)
18 | False | 1 |
20 | False | 2 |
21 | False | 1 |
41 | True | 20 | (41=21*2-1)
42 | False | 1 |
83 | True | 41 | (83=42*2-1)
84 | False | 1 |
167 | True | 83 | (167=84*2-1)
168 | False | 1 |
170 | False | 2 |
171 | False | 1 |
176 | False | 5 |
177 | False | 1 |
353 | True | 176 | (353=177*2-1)
354 | False | 1 |
357 | False | 3 |
368 | False | 11 |
369 | False | 1 |
374 | False | 5 |
375 | False | 1 |
378 | False | 3 |
380 | False | 2 |
381 | False | 1 |
761 | True | 380 | (761=381*2-1)
762 | False | 1 |
1523 | True | 761 | (1523=762*2-1)
1524 | False | 1 |
1529 | False | 5 |
1530 | False | 1 |
1533 | False | 3 |
1535 | False | 2 |
1536 | False | 1 |
1554 | False | 18 |
1560 | False | 6 |
3119 | True | 1559 | (3119=1560*2-1)
3120 | False | 1 |
3128 | False | 8 |
3129 | False | 1 |

Adding a function to check if x is prime shows that only if x is prime do we get a big jump

the only value which breaks this is 6, since 6*2 - 1 = 11 is prime but a new chain does not start at 11

Anwser:
    2744233049300770
--- 11.302829265594482 seconds ---
'''
import time, math
start_time = time.time()

def is_prime(x):  # Test if giving value is a prime
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True
    
def generate_table_for_website(n):
    g = 13
    table = '<table style="width: 100%;text-align: center;" border="2" cellspacing="5"> <tbody> <tr> \
        <td><b>At which n does jump occur</b></td> <td><b>count since last jump</b></td> \
             <td><b>decomposition</b></td> <td><b>is_prime(n)</b></td>'
        
    curr_jump = 1
    for x in range(5, n + 1):
        t = math.gcd(x, g)
        if t == 1:
            curr_jump += 1
        else:
            s = is_prime(x)
            if s:
                table += "<tr>"
                table += '<td style="background-color: #1eeea6;">' + str(x) + "</td>"
                table += '<td style="background-color: #1eeea6;">' + str(curr_jump) + "</td>"
                table += '<td style="background-color: #1eeea6;">' + "(" + str(x) + "=" + str((x + 1)//2) + "*" + str(2) + "-1)" + "</td>"
                table += '<td style="background-color: #1eeea6;">' + str(s) + "</td>"
                table += "</tr>"
                #print(str(x) + " |", str(s) + " |", str(curr_jump) + " |", "(" + str(x) + "=" + str((x + 1)//2) + "*" + str(2) + "-1)")
            else:
                table += "<tr>"
                table += "<td>" + str(x) + "</td>"
                table += "<td>" + str(curr_jump) + "</td>"
                table += "<td> NA </td>"
                table += "<td>" + str(s) + "</td>"
                table += "</tr>"
                #print(str(x) + " |", str(s) + " |", str(curr_jump) + " |")
            curr_jump = 1
        g += t
    table += "</tbody> </table>"
    return table

def g(n):
    curr_g = 13
    for x in range(5, min(7, n + 1)):
        curr_g += math.gcd(x, curr_g)
    
    x = 7
    while x <= n:
        gcd = math.gcd(x, curr_g)
        curr_g += gcd
        
        if gcd > 1:
            t = 2*x - 1
            if is_prime(t):
                if t > n:
                    curr_g += n - x
                    break
                curr_g += x - 2
                x = t - 1

        x += 1
        #print(x, curr_g)
    return curr_g

if __name__ == "__main__":
    print(g(10**15))
    print("--- %s seconds ---" % (time.time() - start_time))
