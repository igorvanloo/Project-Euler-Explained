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
Fibonacci related functions

Author: Igor van Loo
'''

def fibonacci(n):
    '''
    Finds the n-th Fibonacci using matrix exponentiation
    Method is outlined `here <https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series/23462371#23462371>`_

    :param n: An integer

    :returns: The n-th Fibonacci number
    
    .. code-block:: python
    
        print(fibonacci(100)) #354224848179261915075
    '''
    if type(n) != int:
        return "n must be an integer"
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2  
    return v2

def fib_till(limit):
    '''
    Finds all Fibonacci number up till a limit

    :param limit: An integer

    :returns: A list containing all the fibonacci numbers < limit
    
    .. code-block:: python
    
        print(fib_till(100)) #[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        print(sum(fib_till(1000))) #2583
        
    '''
    if type(limit) != int:
        return "limit must be an integer"
    fibnumbers = []
    n = 1
    while fibonacci(n) <= limit:
        fibnumbers.append(fibonacci(n))
        n += 1
    return fibnumbers

def ZeckendorfRepresentation(x):
    '''
    Finds the `Zeckendorf Representation <https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem>`_ of x 

    :param x: An integer

    :returns: A list containing the zeckendorf representation of x
    
    .. code-block:: python
        
        print(ZeckendorfRepresentation(64)) #[55, 8, 1]

    '''
    if type(x) != int:
        return "x must be an integer"
    zeckrep = []
    fibs = fib_till(x)[::-1]
    
    number = x
    count = 0
    while number != 0:
        if number - fibs[count] >= 0:
            number -= fibs[count]
            zeckrep.append(fibs[count])
            count += 1
        count += 1
    return zeckrep