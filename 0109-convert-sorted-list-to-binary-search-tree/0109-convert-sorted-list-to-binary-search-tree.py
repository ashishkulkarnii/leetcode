# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBST(self, arr):
        if not arr:
            return None
        n = len(arr)
        if n == 1:
            return TreeNode(arr[0])
        root = TreeNode(val=arr[n//2], left=self.createBST(arr[:n//2]), right=self.createBST(arr[n//2+1:]))
        return root
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.createBST(arr)