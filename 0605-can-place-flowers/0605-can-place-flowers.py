class Solution:
    def canPlaceFlowers(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        cal=0
        i=1
        if n==0:
            return True
        if n==1:
            if nums[0]==0 and k==1 or k==0:
                return True
            else:
                return False
        if nums[0]==0 and nums[1]==0:
            cal+=1
            nums[0]=1
        if nums[n-1]==0 and nums[n-2]==0:
            cal+=1
            nums[n-1]=1        
        while i<n-1:
            if nums[i-1]==nums[i]==nums[i+1]==0:
                nums[i]=1
                cal+=1
                i+=2
            else:
                i+=1
        
        if cal>=k:
            return True
        return False


            

