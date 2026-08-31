class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def helper(s,L,R):
            if len(s)==2*n:
                res.append(s)
                return
            if L>0:
                helper(s+'(',L-1,R)
            if R>L:
                helper(s+')',L,R-1)
        helper("",n,n)
        return res