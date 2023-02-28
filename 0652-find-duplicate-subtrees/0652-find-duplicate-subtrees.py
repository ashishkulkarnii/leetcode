# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        nodes = collections.defaultdict(list)
        
        def preOrder(node):
            if node == None:
                return "_"
            else:
                traversal = f"{node.val}.{preOrder(node.left)}.{preOrder(node.right)}"
                nodes[traversal].append(node)
                return traversal
        
        preOrder(root)
        return [nodes[i][0] for i in nodes if len(nodes[i]) > 1]
