# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def tr(self, root: Optional[TreeNode]) -> str:
        if(root == None):
            return ""
        else:
            result = []
            result.append(str(root.val))
            if(root.left == None and root.right != None):
                result.append("()")
            elif(root.left != None):
                result.append("(")
                result.append(tr(root, root.left))
                result.append(")")
            if(root.right != None):
                result.append("(")
                result.append(tr(root, root.right))
                result.append(")")
            result = ''.join(result)
            print(result)
            return result
        
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return tr(root, root)
        
        