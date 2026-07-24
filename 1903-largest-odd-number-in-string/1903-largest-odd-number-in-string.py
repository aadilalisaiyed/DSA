class Solution:
    def largestOddNumber(self, num: str) -> str:
        n=len(num)
        while n>0:
            if int(num[-1])%2==1:
                return num
            else:
                num=num[:n-1]
            n-=1
        return ""

