class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        mapp={}
        for i in nums:
            mapp[i]=mapp.get(i,0)+1
        for j in mapp.keys():
            if mapp[j]==1:
                return j
        