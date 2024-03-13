# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:48:01 2024

@author: IP176077
"""
'''
Project Euler Problem 869

2 = 10
3 = 11
5 = 101
7 = 111

Use tree to represent primes

                    start
                 /        \
                /\        / \
                  2      _   3
                        /\   /\
                       _  5  _ 7
                       
Startegy: Pick 0, 1 depending on if the left or right subtree is larger, if your guess is correct
          continue down that subtree, otherwise switch subtree

if p = 2, you will get 1 point
if p = 3, you will get 2 points
if p = 5, you will get 2 points
if p = 7 you will get 3 points

Answer:
    14.97696693
--- 283.2274761199951 seconds --- with E1
--- 89.38337326049805 seconds --- with E
'''

import time, math
start_time = time.time()

class Node:
    def __init__(self, key, left, right):
        self.left = left
        self.right = right
        self.key = key
        
class Tree:
    def __init__(self, root):
        self.root = root
    
    def add_node(self, value):
        binary = bin(value)[2:][::-1]
        curr = self.root
        for b in binary:
            if b == "0":
                if curr.left == None:
                    curr.left = Node([value], None, None)
                    curr.right = Node([], None, None)
                else:
                    curr.left.key += [value]
                curr = curr.left
            
            if b == "1":
                if curr.right == None:
                    curr.right = Node([value], None, None)
                    curr.left = Node([], None, None)
                else:
                    curr.right.key += [value]
                curr = curr.right
    
    def return_height(self, t):
        if t == None:
            return 0
        l = self.return_height(t.left)
        r = self.return_height(t.right)
        return max(r, l) + 1
        
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

def play_game(p, tree):
    if p == 2:
        return 1
    curr = tree.root
    bp = bin(p)[2:][::-1]
    points = 0
    for i in range(len(bp)):
        if len(curr.right.key) >= len(curr.left.key):
            #More likely to be on the right side so we guess 1
            if bp[i] == "1":
                #If we guessed correctly, we get a point and continue down right subtree
                points += 1
                curr = curr.right
            else:
                #Otherwise we continued down left subtree
                curr = curr.left
        else:
            #More likely to be on left side so we guess 0
            if bp[i] == "0":
                points += 1
                curr = curr.left
            else:
                curr = curr.right
    return points
    
def E1(N):
    primes = list_primes(N)
    root = Node("_", None, None)
    tree = Tree(root)
    for p in primes:
        tree.add_node(p)
    print_tree(tree)
    points = 0
    for p in primes:
        points += play_game(p, tree)
    return round(points / len(primes), 8)
        
def _build_tree_string(root, curr_index, index=False, delimiter='-'):
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    if index:
        node_repr = '{}{}{}'.format(curr_index, delimiter, root.key)
    else:
        #try:
            #node_repr = str(root.key) + "(" + str(root.size) + ")"
        #except AttributeError:
        node_repr = str(root.key)

    new_root_width = gap_size = len(node_repr)

    if root.left == root or root.right == root: 
        print("ouch")
        input("frefref")
    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = \
        _build_tree_string(root.left, 2 * curr_index + 1, index, delimiter)
    r_box, r_box_width, r_root_start, r_root_end = \
        _build_tree_string(root.right, 2 * curr_index + 2, index, delimiter)

    # Draw the branch connecting the current root node to the left sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    # Draw the branch connecting the current root node to the right sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(line1), ''.join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end

def print_tree(tree):
    lines = _build_tree_string(tree.root, 0, False, "-")[0]
    print('\n' + '\n'.join((line.rstrip() for line in lines)))
    

def E(N):
    primes = list_primes(N)
    bp = [bin(p)[2:][::-1] for p in primes]
    
    def calc_points(bp):
        if len(bp) == 0:
            return 0
        p0 = []
        p1 = []
        p0_score = 0
        p1_score = 0
        for p in bp:
            if p[0] == "1":
                p1_score += 1
                if len(p) > 1:
                    p1.append(p[1:])
            if p[0] == "0":
                p0_score += 1
                if len(p) > 1:
                    p0.append(p[1:])
        return max(p1_score, p0_score) + calc_points(p0) + calc_points(p1)
    
    return round(calc_points(bp) / len(primes), 8)
    
if __name__ == "__main__":
    print(E(10**8))
    print("--- %s seconds ---" % (time.time() - start_time))
