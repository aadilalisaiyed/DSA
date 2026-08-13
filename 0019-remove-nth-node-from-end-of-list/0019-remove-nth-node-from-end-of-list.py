# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        l=0
        if head.next == None:
            return None
        while temp:
            l+=1
            temp = temp.next
        if n == l:
            return head.next
        op = l-n
        temp = head
        for i in range(op-1):
            temp = temp.next
        temp.next = temp.next.next if temp.next else None
        return head