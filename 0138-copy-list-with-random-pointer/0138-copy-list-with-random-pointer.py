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
        nodes = {}
        curr = head
        dummy = Node(0)
        temp=dummy
        while curr:
            temp.next = Node(curr.val)
            nodes[curr]=temp.next
            curr = curr.next
            temp = temp.next
        curr = head
        temp = dummy.next
        while curr and temp:
            if curr.random:
                temp.random= nodes[curr.random]
            else:
                temp.random=None
            curr= curr.next
            temp= temp.next
        return dummy.next

            