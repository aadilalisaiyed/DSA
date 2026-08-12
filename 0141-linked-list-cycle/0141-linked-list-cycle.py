# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        addr = head
        seen=[]
        while addr and addr not in seen:
            seen.append(addr)
            addr=addr.next
        return addr!=None
