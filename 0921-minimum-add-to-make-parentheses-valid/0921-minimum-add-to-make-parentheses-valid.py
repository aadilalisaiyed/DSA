class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        depth=0
        stack=[]
        ans=0
        for i in s:
            if i=='(':
                stack.append(i)
                depth+=1
            else:
                if stack and stack[-1]=='(':
                    stack.pop()
                    depth-=1
                else:
                    stack.append(i)
                    depth+=1
            
        print(stack)
        x=abs(depth)
        print(x)
        return x