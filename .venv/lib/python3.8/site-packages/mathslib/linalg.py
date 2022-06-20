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
Various Linear Algebra Functions

Author: Igor van Loo
'''

def GaussJordanElimination(matrix, augmentedpart = None):
    '''
    Performs `Gauss Jordan Elimination on the given matrix <https://en.wikipedia.org/wiki/Gaussian_elimination>`_

    :param matrix: Matrix to perform Algoithm on
    :param augmentedpart: Optional addition, will attach the augmented part onto the matrix and then perform the algorithm

    :returns: True if algorithm was successful, false otherwise
    
    .. code-block:: python
    
        matrix = [[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]]
        print(GaussJordanElimination(matrix)) #True
    
    .. note::
        
        This function simply performs the Gauss Jordan Algorithm, it is used with with solve and inverse to solve Ax = b, and the find
        the inverse of a matrix

    '''
    if type(matrix) != list:
        return "matrix must be a list"
    if augmentedpart != None:
        matrix = concatenate(matrix, augmentedpart)
    m, n = len(matrix), len(matrix[0])
    h = 0
    k = 0
    while h < m and k < n:
        i_max = argmax([abs(matrix[i][k]) for i in range(h, m)]) + h
        if matrix[i_max][k] == 0:
            k += 1
        else:
            if h != i_max:
                temp_row = matrix[i_max]
                matrix[i_max] = matrix[h]
                matrix[h] = temp_row
            for i in range(h + 1, m):
                f = matrix[i][k]/matrix[h][k]
                matrix[i][k] = 0
                for j in range(k + 1, n):
                    matrix[i][j] -= f*matrix[h][j]
            h += 1
            k += 1
    for y in range(m-1, -1, -1):
        t = matrix[y][y]
        if abs(t) < pow(10, -10):
            return False
        for z in range(0,y):
            for x in range(n-1, y-1, -1):
                matrix[z][x] -= matrix[y][x] * matrix[z][y] / t
                matrix[z][x] = round(matrix[z][x], 4)
        matrix[y][y] /= t
        matrix[y][y] = round(matrix[y][y], 4)
        for x in range(m, n):
            matrix[y][x] /= t
            matrix[y][x] = round(matrix[y][x], 4)
    return True

def solve(M, b):
    '''
    Finds the solution, x, to the equation Mx = b

    :param M: A Matrix
    :param b: A Vector

    :returns: The Vector x, or an error message
    
    .. code-block:: python
    
        matrix = [[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]]
        b = [[8],
             [-11],
             [-3]]
        print(solve(matrix, b)) #[[2.0], [3.0], [-1.0]]
    
    '''
    if type(M) != list:
        return "M must be a list"
    m, n = len(M), len(M[0])
    if len(b[0]) > 1:
        return "b must be a vector"
    if m != len(b):
        return "Impossible to solve"
    if GaussJordanElimination(M, b):
        return [M[x][n:] for x in range(m)]
    else:
        return "No solution, or infinite solutions"
    
def inverse(matrix):
    '''
    Finds the inverse of the given matrix by performing Gauss Jordan Elimination

    :param matrix: Matrix to be inverted

    :returns: Inverted matrix, or an error message
    
    .. code-block:: python
    
        matrix = [[1, -1, 0], 
                  [-8, 9, -1], 
                  [-9, 0, 10]]
        print(inverse(matrix)) #[[90.0, 10.0, 1.0], [89.0, 10.0, 1.0], [81.0, 9.0, 1.0]]
    
    '''
    if type(matrix) != list:
        return "matrix must be a list"
    m, n = len(matrix), len(matrix[0])
    if m != n:
        return "Must be a square matrix"
    if GaussJordanElimination(matrix, identity(m)):
        return [matrix[x][m:] for x in range(m)]
    else:
        return "Matrix is not invertible"

def determinant(matrix):
    '''
    Finds the determinant of a matrix

    :param matrix: Matrix 

    :returns: det(Matrix)
    
    .. code-block:: python
    
        matrix = [[7, -1, 0], 
                  [-8, 9, -1], 
                  [-9, 0, 10]]
        print(determinant(matrix)) #541.0
    
    '''
    if type(matrix) != list:
        return "matrix must be a list"
    m, n = len(matrix), len(matrix[0])
    if m != n:
        return "Must be a square matrix"
    h = 0
    k = 0
    det = 1
    while h < m and k < n:
        i_max = argmax([abs(matrix[i][k]) for i in range(h, m)]) + h
        if matrix[i_max][k] == 0:
            k += 1
        else:
            if h != i_max:
                temp_row = matrix[i_max]
                matrix[i_max] = matrix[h]
                matrix[h] = temp_row
                det *= -1
            for i in range(h + 1, m):
                f = matrix[i][k]/matrix[h][k]
                matrix[i][k] = 0
                for j in range(k + 1, n):
                    matrix[i][j] -= f*matrix[h][j]
            h += 1
            k += 1  
    for i in range(m):
        det *= matrix[i][i]
    return round(det, 4)

def matrix_addition(A, B, subtract = False):
    '''
    Performs matrix addition/subtraction on matrix A

    :param A: First Matrix 
    :param B: Second Matrix 
    :param subtract: If True, will perform matrix subtraction

    :returns: A + B
    
    .. code-block:: python
    
        matrix = [[1, 0, 0], 
                  [0, 1, 0], 
                  [0, 0, 1]]
        print(matrix_addition(matrix, matrix)) #[[2, 0, 0], [0, 2, 0], [0, 0, 2]]
        print(matrix_addition(matrix, matrix, True)) #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    '''
    if type(A) != list or type(B) != list or type(subtract) != bool:
        return "A and B must be lists"
    m1, n1 = len(A), len(A[0])
    m2, n2 = len(B), len(B[0])
    if m1 != m2 or n1 != n2:
        return "Dimensions are unequal"
    else:
        for x in range(m1):
            for y in range(n1):
                if subtract:
                    A[x][y] -= B[x][y]
                else:
                    A[x][y] += B[x][y]
    return A

def identity(l, val = 1):
    '''
    Generats an Square Identity Matrix

    :param l: Size of matrix
    :param val: diagonal values, default is 1

    :returns: val * identity matrix of size l
    
    .. code-block:: python
    
        print(identity(2)) #[[1, 0], [0, 1]]
        print(identity(2, 5)) #[[5, 0], [0, 5]]
    
    '''
    if type(l) != int or type(val) != int:
        return "l and val must be integers"
    matrix = []
    for x in range(l):
        row = [0]*l
        row[x] = val
        matrix.append(row)
    return matrix

def concatenate(A, B):
    '''
    Concatenates 2 matrices, A and B

    :param A: First Matrix
    :param B: Second Matrix

    :returns: A concatenated with B
    
    .. code-block:: python
    
        A = [[1, 0],
             [0, 1]]
        print(concatenate(A, A)) #[[1, 0, 1, 0], [0, 1, 0, 1]]
    
    .. note::
        
        This is a helper function for inverse and solve
        
    '''
    if type(A) != list or type(B) != list:
        return "A and B must be lists"
    m1 = len(A)
    m2 = len(B)
    if m1 != m2:
        return "Cannot concatenate horizontally"
    for row in range(m1):
        A[row] += B[row]
    return A
    
def argmax(alist):
    '''
    Finds the `argmax <https://en.wikipedia.org/wiki/Arg_max>`_ of a list

    :param alist: A list

    :returns: the arg max of the list
    
    .. code-block:: python
    
        print(argmax([1, 3, 2])) #1
        
    '''
    if type(alist) != list:
        return "Input must be a list"
    f = lambda i: alist[i]
    return max(range(len(alist)), key = f)

def fillmatrix(size, val = 0):
    '''
    Fills a matrix with a value

    :param size: A tuple, denoted (width, height) of matrix
    :param val: Value to fill matrix with, default is 0

    :returns: A matrix
    
    .. code-block:: python
    
        print(fillmatrix((2, 2))) #[[0, 0], [0, 0]]
        print(fillmatrix((2, 3))) #[[0, 0, 0], [0, 0, 0]]
        
    '''
    if type(size) != tuple:
        return "Size must be a tuple"
    return [[val]*size[1] for _ in range(size[0])]
    
def matrix_mul(A, B):
    '''
    Matrix multplication of 2 matrices, A and B

    :param A: First Matrix
    :param B: Second Matrix

    :returns: Matrix AB
    
    .. code-block:: python
    
        A = [[2, 0], 
             [0, 2]]
        B = [[1, 2], 
             [3, 1]]
        print(fillmatrix((A, B))) #[[2, 4], [6, 2]]
        
    '''
    if type(A) != list or type(B) != list:
        return "A and B must be lists"
    m1, n1 = len(A), len(A[0])
    m2, n2 = len(B), len(B[0])
    if n1 != m2:
        return "Cannot multiply matrices"
    matrix = fillmatrix((m1, n2))
    for row in range(m1): 
        for col in range(n2):
            for elt in range(len(B)):
              matrix[row][col] += A[row][elt] * B[elt][col]
    return matrix

