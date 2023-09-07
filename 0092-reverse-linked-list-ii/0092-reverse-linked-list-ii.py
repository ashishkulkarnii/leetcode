# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right == left: return head
        right -= 1
        left -= 1
        original_list = []
        while head:
            original_list.append(head.val)
            head = head.next
        new_list = original_list[:left] + original_list[left:right+1][::-1] + original_list[right+1:]
        new_head = ListNode(new_list[0])
        curr = new_head
        for n in new_list[1:]:
            curr.next = ListNode(n)
            curr = curr.next
        return new_head