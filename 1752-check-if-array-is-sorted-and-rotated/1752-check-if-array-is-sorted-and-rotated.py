class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        idx=-1
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                idx = i+1
        if idx == -1:
            return True
        nums = nums[idx:]+nums[:idx]
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                return False
        return True
