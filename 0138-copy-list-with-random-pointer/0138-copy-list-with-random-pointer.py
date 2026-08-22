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
        if not head:
            return None
        temp = head
        while temp:
            cloned = Node(temp.val,temp.next)
            temp.next=cloned
            temp = cloned.next
        temp = head
        while temp:
            if temp.random:
                temp.next.random=temp.random.next
            temp=temp.next.next
        temp=head
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        return copy_head