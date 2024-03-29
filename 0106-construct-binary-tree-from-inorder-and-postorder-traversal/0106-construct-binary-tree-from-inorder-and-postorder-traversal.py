# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder):
        self.buildTree1(inorder, postorder, root:=TreeNode(postorder[-1]))
        return root
    def buildTree1(self, inorder: List[int], postorder: List[int], node):
        if not node:
            return
        node_pos = inorder.index(node.val)
        if left_subtree_inorder := inorder[:node_pos]:
            node.left = TreeNode((left_subtree_postorder:=postorder[:len(left_subtree_inorder)])[-1])
            self.buildTree1(left_subtree_inorder, left_subtree_postorder, node.left)
        if right_subtree_inorder := inorder[node_pos+1:]:
            node.right = TreeNode((right_subtree_postorder:=postorder[len(left_subtree_inorder):-1])[-1])
            self.buildTree1(right_subtree_inorder, right_subtree_postorder, node.right)
