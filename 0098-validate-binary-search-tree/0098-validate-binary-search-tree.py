# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root, inorder):
        if root == None:
            return
        self.inOrder(root.left, inorder)
        inorder.append(root.val)
        self.inOrder(root.right, inorder)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = list()
        self.inOrder(root, inorder)
        if len(inorder) == 1:
            return True
        for index, value in enumerate(inorder[:-1:]):
            if value >= inorder[index + 1]:
                return False
        return True