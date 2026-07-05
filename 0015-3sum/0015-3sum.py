class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for fix in range(n-2):
            l= fix + 1
            r = n-1
            if fix>0 and nums[fix]==nums[fix-1]:
                continue
            while(l<r):
                s = nums[fix]+nums[l]+nums[r]
                if s == 0:
                    ans.append([nums[fix],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif s > 0:
                    r-=1
                else:
                    l+=1        
        print(ans)
        return ans
                


