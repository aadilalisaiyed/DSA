class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans=[]
        nums.sort()
        for f1 in range(n-3):
            if f1>0 and nums[f1]==nums[f1-1]:
                continue

            for f2 in range(f1+1,n-2):
                if f2>f1+1 and nums[f2]==nums[f2-1]:
                    continue
                l=f2+1
                r=n-1
                while l<r:
                    s = nums[f1]+nums[f2]+nums[l]+nums[r]
                    if s == target:
                        ans.append([nums[f1],nums[f2],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                    elif s > target:
                        r-=1
                    else:
                        l+=1
        return ans

        