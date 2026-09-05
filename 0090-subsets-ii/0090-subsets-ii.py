class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def backtrack(idx,subarr):
            if idx == len(nums):
                res.append(subarr[:])
                return
            subarr.append(nums[idx])
            backtrack(idx+1,subarr)
            subarr.pop()

            nextIdx=idx+1
            while nextIdx<len(nums) and nums[idx]==nums[nextIdx]:
                nextIdx+=1
            backtrack(nextIdx,subarr)
        backtrack(0,[])
        return res            