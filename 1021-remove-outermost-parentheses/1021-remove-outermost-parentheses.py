class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        depth=0
        ans=""
        for i in range(n):
            if s[i]=='(':
                if depth > 0:
                    ans+=s[i]
                depth+=1
            else:
                depth-=1
                if depth > 0:
                    ans+=s[i]
        return ans
            