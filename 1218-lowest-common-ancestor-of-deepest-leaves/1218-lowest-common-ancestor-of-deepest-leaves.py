# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        subtree = {}
        def dfs(node, d=0):
            if node:
                subtree[node.val] = max(dfs(node.left, d + 1), dfs(node.right, d + 1)) + 1
                return subtree[node.val]
            else:
                return -1
        dfs(root)
        def get_lca(node):
            if subtree[node.val] == 0:
                return node
            lsub = subtree[node.left.val] + 1 if node.left else 0
            rsub = subtree[node.right.val] + 1 if node.right else 0
            if lsub == rsub:
                return node
            elif lsub > rsub:
                return get_lca(node.left)
            elif rsub > lsub:
                return get_lca(node.right)
        return get_lca(root)
