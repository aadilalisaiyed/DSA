# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1 or head is None or head.next is None:
            return head
        def reverse(head,end):
            curr = head
            prev = None
            while curr and curr != end:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        start = end = head
        start_prev=end_prev = None
        while True:
            c=1
            while end and c<k:
                end_prev = end
                c+=1
                end=end.next

            if end is None:
                break
            prev = reverse(start,end)
            if start_prev:
                start_prev.next=end
            else:
                head=end
            start.next=end.next
            end.next=end_prev
            start_prev = start
            start = start.next
            end= start
        return head

        
        