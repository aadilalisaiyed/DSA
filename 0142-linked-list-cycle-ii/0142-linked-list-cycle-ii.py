# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        addr=head
        seen=[]
        while addr:
            if addr in seen:
                return addr
            seen.append(addr)
            addr = addr.next
        return None
