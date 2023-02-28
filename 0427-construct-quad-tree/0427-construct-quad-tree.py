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
        return Node(False, False, self.buildTree(grid[:len(grid)//2, :len(grid)//2]), self.buildTree(grid[:len(grid)//2, len(grid)//2:]), self.buildTree(grid[len(grid)//2:, :len(grid)//2]), self.buildTree(grid[len(grid)//2:, len(grid)//2:]))
    
    def construct(self, grid: List[List[int]]) -> 'Node':
        return None if not grid else self.buildTree(np.array(grid))