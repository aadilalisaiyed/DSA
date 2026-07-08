class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        nums.sort()
        ans=[]
        n = len(nums)
        for i in range(n):
            start=nums[i][0]
            end = nums[i][1]
            if ans and end <= ans[-1][1]:
                continue
            for j in range(i+1,n):
                if end >= nums[j][0]:
                    end = max(end,nums[j][1])
                else:
                    break
            ans.append([start,end])
        return ans   
            
            