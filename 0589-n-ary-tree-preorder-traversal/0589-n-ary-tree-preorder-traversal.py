"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        return [] if root == None else [root.val] + list(itertools.chain(*list(map(self.preorder, root.children))))