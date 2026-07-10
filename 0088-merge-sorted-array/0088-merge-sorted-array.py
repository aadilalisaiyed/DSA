class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m+n-1
        p = m-1
        q = n-1
        
        while q>=0:
            if nums1[p] >= nums2[q] and p>=0:
                nums1[k]=nums1[p]
                p-=1
            else:
                nums1[k]=nums2[q]
                q-=1
            k-=1
        if p==0:
            for i in range(q):
                nums1[i]=nums2[i]
