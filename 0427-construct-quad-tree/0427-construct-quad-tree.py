"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
import numpy as np

class Solution:
    def buildTree(self, grid):
        if len(grid) ** 2 == np.count_nonzero(grid == 1) or len(grid) ** 2 == np.count_nonzero(grid == 0):
            return Node(grid[0][0], True, None, None, None, None)
        q1 = grid[:len(grid)//2, len(grid)//2:]
        q2 = grid[:len(grid)//2, :len(grid)//2]
        q3 = grid[len(grid)//2:, :len(grid)//2]
        q4 = grid[len(grid)//2:, len(grid)//2:]
        tr = self.buildTree(q1)
        tl = self.buildTree(q2)
        bl = self.buildTree(q3)
        br = self.buildTree(q4)
        return Node(False, False, tl, tr, bl, br)
    
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None
        grid = np.array(grid)
        return self.buildTree(grid)