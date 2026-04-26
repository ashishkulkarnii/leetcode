# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        def rec(node):
            if not node:
                return 0
            return int(node.val == p.val) + int(node.val == q.val) + rec(node.left) + rec(node.right)
        while curr:
            if curr.val == p.val or curr.val == q.val:
                return curr
            else:
                l = rec(curr.left)
                if l == 1:
                    return curr
                elif l == 2:
                    curr = curr.left
                else:
                    curr = curr.right