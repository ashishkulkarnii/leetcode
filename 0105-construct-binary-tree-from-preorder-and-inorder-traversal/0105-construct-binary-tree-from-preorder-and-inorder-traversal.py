# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        self.buildTree1(inorder, preorder, root)
        return root
    def buildTree1(self, inorder: List[int], preorder: List[int], node):
        if not node:
            return
        node_pos = inorder.index(node.val)
        left_subtree_inorder = inorder[:node_pos]
        left_subtree_preorder = preorder[1:len(left_subtree_inorder)+1]
        right_subtree_inorder = inorder[node_pos+1:]
        right_subtree_preorder = preorder[len(left_subtree_inorder)+1:]
        if left_subtree_inorder:
            node.left = TreeNode(left_subtree_preorder[0])
            self.buildTree1(left_subtree_inorder, left_subtree_preorder, node.left)
        if right_subtree_inorder:
            node.right = TreeNode(right_subtree_preorder[0])
            self.buildTree1(right_subtree_inorder, right_subtree_preorder, node.right)