class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_count = [0]*31
        #making buckets for each bit (till 30 bits) having count of no. of each bits in all elts nums
        for i in nums:
            for j in range(31):
                if (i>>j)&1==1:
                    bit_count[j]+=1
        #distributing for k elts
        res=[0]*k
        for i in range(30,-1,-1):
            curr = bit_count[i]
            for j in range(min(curr,k)):
                res[j]|=(1<<i)
        #total
        ans=0
        for x in res:
            ans=(ans + x**2)%MOD
        print(ans)
        return ans
        