# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        val_lev = collections.defaultdict(list)
        def bfs(node, level):
            if not node: return
            val_lev[level].append(node.val)
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)
        bfs(root, 0)
        res = [i for i in val_lev.values()]
        return res