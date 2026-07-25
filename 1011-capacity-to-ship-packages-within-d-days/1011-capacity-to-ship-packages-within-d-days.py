class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n=len(weights)
        # best case : days == n so we need max(weights) storage
        # worst case: days == 1 so we need sum(weights) storage
        l,r=max(weights),sum(weights)
        final = r
        while l<=r:
            mid = (l+r)//2
            cal_d=1
            curr_sum=0
            for i in range(n):
                if curr_sum+weights[i] > mid:
                    cal_d+=1
                    curr_sum=0
                curr_sum+=weights[i]
            if cal_d <= days:
                final = mid
                r=mid-1
            else:
                l=mid+1
        return final
                
                