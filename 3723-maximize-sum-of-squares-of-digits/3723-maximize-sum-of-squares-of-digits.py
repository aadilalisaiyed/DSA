class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans=""
        while num>0:
            curr=min(9,sum)
            ans+=str(curr)
            sum-=curr
            num-=1
        if sum!=0:
            return ""
        return ans