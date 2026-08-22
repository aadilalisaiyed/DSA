# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        L=0
        curr = head
        end = head
        if head is None or head.next is None:
            return head
        while curr:
            end = curr
            L+=1
            curr = curr.next
        end.next = head
        k%=L
        moves = L-k-1
        if moves == -1:
            return head
        temp=head
        for i in range(moves):
            temp = temp.next
        ans=temp.next
        temp.next = None
        return ans
