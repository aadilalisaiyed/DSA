class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        Total_subarray=1<<n
        res=[]
        for i in range(Total_subarray):
            subset=[]
            for j in range(n):
                if i&(1<<j):
                    subset.append(nums[j])
            res.append(subset)
        return res