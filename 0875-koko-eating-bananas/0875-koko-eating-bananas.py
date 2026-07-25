class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        maxi=max(piles)
        l,r=1,maxi
        final=r
        while l<=r:
            mid = (l+r)//2
            ans=0
            for i in range(n):
                ans+=(piles[i]+mid-1)//mid
            if ans<=h:
                final = mid
                r=mid-1
            else:
                l=mid+1
        return final
                
            