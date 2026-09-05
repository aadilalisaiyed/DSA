class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(idx,target,subarr):
            if target==0:
                res.append(subarr[:])
                return
            if target<0 or idx == len(candidates):
                return
            subarr.append(candidates[idx]) # PICK
            backtrack(idx+1,target-candidates[idx],subarr) #Explore PICK
            subarr.pop() # UNDO PICK
            nextidx=idx+1
            while nextidx<len(candidates) and candidates[idx]==candidates[nextidx]:
                nextidx+=1
            backtrack(nextidx,target,subarr) # Explore NOT PICK
        backtrack(0,target,[])
        return res
