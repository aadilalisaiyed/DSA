class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        s=0
        for f in range(n):
            if nums[f]!=0:
                nums[s],nums[f]=nums[f],nums[s]
                s+=1
        