class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        depth=0
        stack=[]
        ans=0
        for i in s:
            if i=='(':
                stack.append(i)
            else:
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)
            
        x=len(stack)
        return x