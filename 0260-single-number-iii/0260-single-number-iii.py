class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        x=0
        for i in nums:
            x^=i
        first1=(x & (x-1))^x
        buck1=buck2=0
        for i in nums:
            if i&first1 == first1:
                buck1^=i
            else:
                buck2^=i
        return [buck1,buck2]