class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        l,m,h=0,0,n-1
        while m<=h:
            if nums[m]==2:
                nums[m],nums[h]=nums[h],nums[m]
                h-=1
            elif nums[m]==0:
                nums[m],nums[l]=nums[l],nums[m]
                l+=1
                m+=1
            else:
                m+=1
            