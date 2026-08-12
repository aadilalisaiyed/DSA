# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = deque()
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
        temp=head
        while temp:
            if stack and temp.val == stack[-1]:
                stack.pop()
            temp=temp.next
        if len(stack)==0:
            return True
        else:
            return False

        