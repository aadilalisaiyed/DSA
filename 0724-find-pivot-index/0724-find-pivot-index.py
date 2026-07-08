class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pref=[0]*n
        suff=[0]*n
        pref[0]=nums[0]
        suff[n-1]=nums[n-1]
        for i in range(1,n):
            pref[i]=pref[i-1]+nums[i]
        for i in range(n-2,-1,-1):
            suff[i]=suff[i+1]+nums[i]
        print(pref)
        print(suff)
        for i in range(n):
            if pref[i] == suff[i]:
                return i
        return -1