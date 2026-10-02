class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        if n==1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        for i in range(1,n-1):
            if nums[i]!= nums[i-1] and nums[i]!= nums[i+1]:
                return nums[i]
        if nums[-2]!=nums[-1]:
            return nums[-1]