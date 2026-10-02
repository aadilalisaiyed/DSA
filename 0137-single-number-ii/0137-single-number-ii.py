class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res=0
        for i in range(32):
            curr=0
            for j in nums:
                curr+= ((j>>i) & 1)
            if curr%3==1:
                curr%=3
                res|= curr<<i
            if res>=2**31:
                res-=2**32
        return res
