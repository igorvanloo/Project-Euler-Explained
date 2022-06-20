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
Various known algorithms. They are graph theory and optimization related

Author: Igor van Loo
'''
def PrimsAlgorithm(matrix):
    '''
    Implementation of `Prim's algorithm <https://en.wikipedia.org/wiki/Prim%27s_algorithm>`_
    It finds a Minimum Spanning Tree (MST) for a weighted undirected graph.
        
    :param matrix: Takes a `Adjacency matrix <https://en.wikipedia.org/wiki/Adjacency_matrix>`_ as input
    
    :returns Weight: The sum of the minimum spanning tree
    :returns mask: The corresponding Adjacency matrix of the MST
    
    Example from Project `Euler Problem 107 <https://projecteuler.net/problem=107>`_
    
    .. code:: python
        
        matrix = [[0, 16, 12, 21, 0, 0, 0], 
                  [16, 0, 0, 17, 20, 0, 0], 
                  [12, 0, 0, 28, 0, 31, 0], 
                  [21, 17, 28, 0, 18, 19, 23], 
                  [0, 20, 0, 18, 0, 0, 11], 
                  [0, 0, 31, 19, 0, 0, 27], 
                  [0, 0, 0, 23, 11, 27, 0]]
        
        print(PrimsAlgorithm(matrix)) #(93, 
                                      #[[0, 16, 12, 0, 0, 0, 0],
                                      #[16, 0, 0, 17, 0, 0, 0],
                                      #[12, 0, 0, 0, 0, 0, 0],
                                      #[0, 17, 0, 0, 18, 19, 0],
                                      #[0, 0, 0, 18, 0, 0, 11],
                                      #[0, 0, 0, 19, 0, 0, 0],
                                      #[0, 0, 0, 0, 11, 0, 0]])
    
    '''
    dimension = len(matrix)
    mask = [[0 for x in range(len(matrix[0]))] for x in range(dimension)]
    Tree = set([0])
    Weight = 0    
    for x in range(dimension - 1):
        Minimum_edge, a, b = min([(matrix[x][y], x, y) for x in Tree for y in range(dimension) if y not in Tree and matrix[x][y] != 0])
        Tree.add(b)
        mask[a][b] = matrix[a][b]
        mask[b][a] = matrix[a][b]
        Weight += Minimum_edge
        if len(Tree) == dimension:
            break
    return Weight, mask

def DijkstrasAlgorithm(matrix, start_node = (0, 0), end_node = (-1, -1)):
    '''
    Implementation of `Dijkstra's algorithm <https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm>`_ 
    It finds the the shortest paths between nodes in a graph

    :param matrix: Takes a matrix as imput
    :param start_node: Optional tuple, it is initially set as the top left corner of matrix
    :param end_node: Optional tuple, it is initially set as the bottom right corner of matrix

    :returns: Shortest path between desired starting and ending node
    
    .. note::
        
        The matrix assumes that each vertex has an edge to it's neighbour, therefore this is not a widely applicable case
        
    Example from Project `Euler Problem 83 <https://projecteuler.net/problem=83>`_
    
    .. code:: python
    
        matrix = [[131, 673, 234, 103,18],
                 [201, 96, 342, 965, 150],
                 [630, 803, 746, 422, 111],
                 [537, 699, 497, 121, 956],
                 [805, 732, 524, 37, 331]]
        
        print(DijkstrasAlgorithm(matrix)) #2297
        
    '''
    rows = len(matrix)
    columns = len(matrix[0])
    INF = 10**8    
    unvisisted_nodes = dict()
    for x in range(rows):
        for y in range(columns):
            unvisisted_nodes[(x, y)] = INF
    unvisisted_nodes[(0, 0)] = matrix[0][0]    
    mask = [[INF]*columns for i in range(rows)]
    mask[0][0] = matrix[0][0]  
    
    def visit_neighbour(og_x, og_y, x, y, unvisisted_nodes):
        if x < 0 or x >= rows or y < 0 or y >= columns:
            return False
        if (x, y) in unvisisted_nodes:
            return min(mask[x][y], mask[og_x][og_y] + matrix[x][y])
        
    curr = start_node #Starting node
    while True:
        x, y = curr
        for (a, b) in ((x + 1, y), (x, y+ 1), (x - 1, y), (x, y - 1)):
            temp = visit_neighbour(x, y, a, b, unvisisted_nodes)
            if temp:
                mask[a][b] = temp
                unvisisted_nodes[(a, b)] = temp
        unvisisted_nodes.pop(curr)        
        if len(unvisisted_nodes) != 0:
            curr = min(unvisisted_nodes, key=unvisisted_nodes.get)
        else:
            break
    if end_node == (-1, -1):
        return mask[rows - 1][columns - 1] #Ending node
    else:
        a, b = end_node
        return mask[a - 1][b - 1]

def KnapSack(values, weights, n, W, no_values = True):
    '''
    Implementation of dynamic programming solution to the 0-1 `Knapsack Problem <https://en.wikipedia.org/wiki/Knapsack_problem>`_
    
    :param values: A list of values
    :param weights: A list with weight of corresponding values
    :param n: Number of items
    :param W: Desired weight
    :param no_values: Optional boolean value
        
    :returns:
        * If no_values == True - It returns the optimal sum of weights
        * If no_values == False - it returns the entire array used to build up the solution
        
    .. code-block:: python
        
        values = [60, 100, 120]
        weights = [10, 20, 30]
        W = 50
        n = len(values)
        
        print(KnapSack(values, weights, n, W)) #220
    '''
    array = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                array[i][j] = 0
                
            elif weights[i - 1] > j:
                array[i][j] = array[i-1][j]
            else:
                array[i][j] = max(array[i - 1][j], array[i - 1][j - weights[i - 1]] + values[i - 1])
    
    if no_values:
        return array[n][W]
    
    if no_values == False:
        return array
    
def KnapSackValues(values, weights, n, W):
    '''
    Extension to KnapSack function
    It finds the actual values used to obtain the optimal sum

    :param values: A list of values
    :param weights: A list with weight of corresponding values
    :param n: Number of items
    :param W: Desired weight

    :returns: A set with the optimal values which form the solution to the knapsack problem
    
    .. code-block:: python
        
        values = [60, 100, 120]
        weights = [10, 20, 30]
        W = 50
        n = len(values)
        
        print(KnapSackValues(values, weights, n, W)) #{20, 30}
    
    '''
    array = KnapSack(values, weights, n, W, no_values = False)
    if n == 0:
        return {}
    if array[n][W] > array[n - 1][W]:
        return {weights[n - 1]}.union(KnapSackValues(values, weights, n - 1, W - weights[n - 1]))
    else:
        return KnapSackValues(values, weights, n - 1, W - weights[n - 1])
    
    
    