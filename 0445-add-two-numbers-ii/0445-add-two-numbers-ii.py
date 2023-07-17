def tolist(self):
    curr = self
    res = []
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

ListNode.tolist = tolist


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        carry = 0
        for a, b in list(itertools.zip_longest(l1.tolist()[::-1], l2.tolist()[::-1], fillvalue=0)):
            res.append((a + b + carry) % 10)
            carry = (a + b + carry) // 10
        if carry:
            res.append(carry)
        head = ListNode(res.pop(-1))
        curr = head
        while res:
            curr.next = ListNode(res.pop(-1))
            curr = curr.next
        return head
