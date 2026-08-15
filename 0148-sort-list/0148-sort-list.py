# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def middle(head):
            slow,fast=head,head.next
            while fast and fast.next:
                slow=slow.next
                fast = fast.next.next
            return slow
        def merge(L1,L2):
            dummy = ListNode()
            tail = dummy
            
            while L1 and L2:
                if L1.val < L2.val:
                    tail.next=L1
                    L1=L1.next
                else:
                    tail.next = L2
                    L2=L2.next
                tail = tail.next
            if L1:
                tail.next = L1
            else:
                tail.next = L2
            return dummy.next     

        def mergeSort(head):
            if head is None or head.next is None:
                return head
            mid = middle(head)
            LeftHead = head
            RightHead = mid.next
            mid.next=None
            SortedL=mergeSort(LeftHead)
            SortedR=mergeSort(RightHead)
            return merge(SortedL,SortedR)
        return mergeSort(head)
        