# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        appeared = set()
        appeared.add(head.val)
        curr = head
        while curr.next != None:
            if curr.next.val not in appeared:
                appeared.add(curr.next.val)
                curr = curr.next
            else:
                curr.next = curr.next.next
        return head