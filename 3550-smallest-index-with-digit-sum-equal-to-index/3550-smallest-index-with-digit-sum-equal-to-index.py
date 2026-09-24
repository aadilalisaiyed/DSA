class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sod(x):
            res=0
            while x>0:
                res+=(x%10)
                x//=10
            return res
            
        n=len(nums)
        for i in range(n):
            sumi = sod(nums[i])
            if sumi==i:
                return i
        return -1
        