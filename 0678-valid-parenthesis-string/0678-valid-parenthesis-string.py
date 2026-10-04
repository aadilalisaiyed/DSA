class Solution:
    def checkValidString(self, s: str) -> bool:
        memo={}
        def helper(idx,open):
            if open<0:
                return False
            if idx == len(s):
                return open == 0
            state=(idx,open)
            if state in memo:
                return memo[state]
            if s[idx]=='(':
                res= helper(idx+1,open+1)
            elif s[idx]==')':
                res= helper(idx+1,open-1)
            else:
                res= (helper(idx+1,open) or helper(idx+1,open-1) or helper(idx+1,open+1))
            memo[state]=res
            return res
        return helper(0,0)
            
        

            
