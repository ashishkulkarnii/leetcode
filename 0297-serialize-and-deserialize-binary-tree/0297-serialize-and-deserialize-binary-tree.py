# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        res = []
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr:
                res.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                res.append(curr)
        return ",".join([str(v) for v in res])
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        root = TreeNode(data[0])
        queue = [root]
        i = 1
        while i < len(data):
            curr = queue.pop(0)
            if data[i] != "None":
                curr.left = TreeNode(int(data[i]))
                queue.append(curr.left)
            i += 1
            if data[i] != "None":
                curr.right = TreeNode(int(data[i]))
                queue.append(curr.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))