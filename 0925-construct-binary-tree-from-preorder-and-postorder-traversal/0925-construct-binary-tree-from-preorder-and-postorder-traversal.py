# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def get_left(node_val):
            for i, v in enumerate(preorder[:-1]):
                if v == node_val:
                    return preorder[i+1]
            return None
        def get_right(node_val):
            for i, v in enumerate(postorder):
                if v == node_val and i > 0:
                    return postorder[i-1]
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        queue = [root]
        used = set()
        used.add(root_val)
        while queue:
            curr = queue.pop()
            lv = get_left(curr.val)
            if lv and lv not in used:
                curr.left = TreeNode(lv)
                queue.append(curr.left)
                used.add(lv)
            rv = get_right(curr.val)
            if rv and rv not in used:
                curr.right = TreeNode(rv)
                queue.append(curr.right)
                used.add(rv)
        return root