"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        copy_head = Node(curr.val) if curr else None
        copy_curr = copy_head
        copy_map = dict()
        while curr:
            copy_map[curr] = copy_curr
            if curr.next:
                copy_curr.next = Node(curr.next.val)
            else:
                copy_curr.next = None
            copy_curr = copy_curr.next
            curr = curr.next
                
        curr = head
        copy_curr = copy_head
        while curr:
            copy_curr.random = copy_map.get(curr.random, None)
            copy_curr = copy_curr.next
            curr = curr.next

        return copy_head