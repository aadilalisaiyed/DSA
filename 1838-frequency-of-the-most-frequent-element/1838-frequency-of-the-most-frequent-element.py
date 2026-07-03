class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        ans = 1
        nums.sort()
        l=0
        windowSum=0
        
        for r in range(n):
            windowSum+=nums[r]
            while nums[r]*(r-l+1) - windowSum > k:
                windowSum-=nums[l]
                l+=1
            ans = max(ans,r-l+1)
        return ans
        