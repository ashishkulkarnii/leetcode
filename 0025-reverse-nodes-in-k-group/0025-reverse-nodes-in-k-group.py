# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def list2List(self, arr: list) -> Optional[ListNode]:
        head = ListNode(arr[0])
        res = head
        for val in arr[1::]:
            head.next = ListNode(val)
            head = head.next
        return res
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        while(head):
            arr.append(head.val)
            head = head.next
        if not arr:
            return None
        for i in range(k, len(arr) + 1, k):
            arr[i-k:i:] = arr[i-k:i:][::-1]
        return self.list2List(arr)