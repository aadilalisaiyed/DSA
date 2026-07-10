class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP=1
        ans = float('-inf')
        n=len(nums)
        for i in range(n):
            
            maxP*=nums[i]
            ans = max(maxP,ans)
            if maxP==0:
                maxP=1
        maxP=1
        for i in range(n-1,-1,-1):
            maxP*=nums[i]
            ans = max(maxP,ans)
            if maxP==0:
                maxP=1
        return ans
