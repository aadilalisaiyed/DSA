class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        maxi=max(nums)
        l,r=1,maxi
        final=r
        while l<=r:
            mid = (l+r)//2
            cal_t=0
            for i in range(n):
                cal_t += (nums[i]+mid-1)//mid
            if cal_t <= threshold:
                final = mid
                r=mid-1
            else:
                l=mid+1
        return final

