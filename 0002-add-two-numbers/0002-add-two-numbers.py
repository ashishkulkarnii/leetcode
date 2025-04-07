# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode()
        carry = 0
        res = l
        while l1 and l2:
            l.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            if l1 and not l2:
                l2 = ListNode()
            elif l2 and not l1:
                l1 = ListNode()
            if not l1 and not l2 and carry:
                l1 = l2 = ListNode()
            l = l.next
        if carry:
            l.next = ListNode(carry)
        return res.next