class Solution:
    def mergesort(self,nums):
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left = self.mergesort(nums[:mid])
        right = self.mergesort(nums[mid:])
        return self.merge(left,right)
    def merge(self,L,R):
        i=j=0
        ans=[]
        n1 = len(L)
        
        while i<n1 and j<len(R):
            
            if L[i]<=R[j]:
                ans.append(L[i])
                i+=1
            else:
                ans.append(R[j])
                j+=1
        
        ans.extend(L[i:])
        ans.extend(R[j:])
        j=0
        for i in range(n1):
            while j<len(R) and L[i]>2*R[j]:
                j+=1
            self.c+=j
        return ans

    def reversePairs(self, nums: List[int]) -> int:
        self.c =0
        self.mergesort(nums)
        return self.c
