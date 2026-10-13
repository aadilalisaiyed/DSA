class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1
        for i in range(n):
            nums[i]=abs(nums[i])
        nums.sort()
        while l<r:
            if r%2==0:
                r-=1
            else:
                if nums[l]<nums[r]:
                    nums[l],nums[r]=nums[r],nums[l]
                    r-=1
                l+=2
        total=0
        for i in range(n):
            if i%2==0:
                total+=(nums[i]**2)
            else:
                total-=(nums[i]**2)
        return total

        
                