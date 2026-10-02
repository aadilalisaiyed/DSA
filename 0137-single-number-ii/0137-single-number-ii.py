class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res=0
        for i in range(32):
            currsum=0
            for j in nums:
                currsum+= (j>>i &1)
            currsum%=3
            res |= currsum<<i
        if res>=2**31:
            res-=2**32
        return res