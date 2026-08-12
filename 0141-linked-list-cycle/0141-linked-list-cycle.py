# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        addr = head
        seen=set()
        while addr:
            if addr in seen:
                return True
            seen.add(addr)
            addr=addr.next
        return False
