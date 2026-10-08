class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        depth=0
        ans=""
        for i in s:
            
            if i =='(':
                if depth>0:
                    ans+=i
                depth+=1
            else:
                depth-=1
                if depth>0:
                    ans+=i
        return ans