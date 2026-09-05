class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def helper(idx,t,subarr):
            print(subarr)
            if t == 0:
                res.append(subarr)
                return

            if idx == len(candidates):
                return
            if candidates[idx]>t:
                return
            helper(idx,t-candidates[idx],subarr+[candidates[idx]]) # PICK
            helper(idx+1,t,subarr) # NOT PICK
        helper(0,target,[])
        return res
