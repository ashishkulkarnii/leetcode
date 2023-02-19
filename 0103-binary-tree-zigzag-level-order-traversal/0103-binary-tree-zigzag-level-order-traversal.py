# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        direction = 1
        level_count = 1
        result = []
        
        while queue:
            level = queue[:level_count:]
            queue = queue[level_count::]
            
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            temp = []
            for node in level[::direction]:
                temp.append(node.val)
            result.append(temp)
            
            level_count *= 2
            direction *= -1
        return result