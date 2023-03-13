# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode], root2=None) -> bool:
        return self.isSymmetricRec(root.left, root.right)
    def isSymmetricRec(self, root: Optional[TreeNode], root2) -> bool:
        if root == root2 == None:
            return True
        elif root and not root2 or not root and root2:
            return False
        elif root.val != root2.val:
            return False
        else:
            return self.isSymmetricRec(root.left, root2.right) and self.isSymmetricRec(root.right, root2.left)