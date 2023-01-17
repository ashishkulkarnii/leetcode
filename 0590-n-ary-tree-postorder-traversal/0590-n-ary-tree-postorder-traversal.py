"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        return [] if root == None else list(itertools.chain(*list(map(self.postorder, root.children)))) + [root.val]