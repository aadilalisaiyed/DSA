class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l,r=max(nums),sum(nums)
        final=r
        while l<=r:
            mid=(l+r)//2
            cal_k=1
            pref=0
            for i in range(n):
                if pref+nums[i]>mid:
                    cal_k+=1
                    pref=nums[i]
                else:
                    pref+=nums[i]
            if cal_k > k:
                l=mid+1
            else:
                final = mid
                r=mid-1
        return final
