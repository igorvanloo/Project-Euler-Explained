# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <https://unlicense.org>


'''
Various simple functions

Author: Igor van Loo
'''
import math

def n_choose_r(n, r):
    '''
    n choose r function

    :param n: An integer
    :param r: An integer

    :returns: n choose r
    
    .. code-block:: python
    
        print(n_choose_r(50, 30)) #47129212243960
        
    '''
    if r > n:
        return "n must be greter than r"
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))
    
def numberToBase(n, b):
    '''
    Changes n from base 10 to base b

    :param n: An integer, number to be changed
    :param b: An integer, base in question

    :returns: n in base b
        
    .. code-block:: python
    
        print(numberToBase(10, 2)) #[1, 0, 1, 0]
        print(numberToBase(10, 3)) #[1, 0, 1]
        
    '''
    if (type(n) != int) or (type(b) != int):
        return "n and b must be an integer"
    if n == 0:
        return [0]
    digits = []
    while n != 0:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def lcm(a_list):
    '''
    Finds the lcm of a list of numbers

    :param alist: A list containing integers

    :returns: The lcm of all numbers in the list
    
    .. code-block:: python
    
        print(lcm([2, 3])) #6
        print(lcm([2, 4, 5, 7])) #140
        print(lcm([8345, 23579, 174])) #34237415370
        
    '''
    n = sorted(a_list)
    curr = n.pop(-1)
    while len(n) != 0:
        temp = n.pop(-1)
        curr = int(abs(curr*temp)/math.gcd(curr, temp))
    return curr

def ModDivision(a, b, m):
    '''
    Finds a/b mod m

    :param a: An integer, the numerator
    :param b: An integer, the denominator
    :param m: An integer, the modulus

    :returns: a/b mod m
    
    .. code-block:: python
    
        print(ModDivision(8, 4, 5)) #2
        
    '''
    if (type(a) != int) or (type(b) != int) or (type(m) != int):
        return "n and b must be an integer"
    try:
        inv = pow(b, -1, m)
    except ValueError:
        if a % b == 0:
            answer = (a % m * b) // b
    else:
        a = a % m
        answer = (inv * a) % m
    return answer

