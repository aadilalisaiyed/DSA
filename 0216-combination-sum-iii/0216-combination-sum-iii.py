class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def helper(k,n,val,subarr):
            if n==0 and k==0:
                res.append(subarr[:])
                return
            if n<0 or val>9:
                return
            # PICK
            subarr.append(val)
            helper(k-1,n-val,val+1,subarr)
            subarr.pop()

            #NOT PICK
            helper(k,n,val+1,subarr)
        helper(k,n,1,[])
        return res


