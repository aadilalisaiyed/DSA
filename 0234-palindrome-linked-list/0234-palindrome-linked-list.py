# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        def rev(head):
            temp = head
            prev= None
            while temp:
                next = temp.next
                temp.next=prev
                prev=temp
                temp=next
            return prev                
        middle = rev(middle)
        p1,p2 = head,middle
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2=p2.next
        return True
        

        