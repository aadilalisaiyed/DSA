# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n=m=0
        temp = headA
        while temp:
            n+=1
            temp=temp.next
        temp = headB
        while temp:
            m+=1
            temp=temp.next
        if n<m:
            return self.getIntersectionNode(headB,headA)
        tempA=headA
        while n>m:
            tempA=tempA.next
            n-=1
        tempB=headB
        for i in range(n):
            if tempA == tempB:
                return tempA
            tempA=tempA.next
            tempB=tempB.next
        return None