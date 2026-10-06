class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        isc= False #Tracks whether the parentheses is consecutive or not 
        stack=[0]
        for i in s:
            if i=='(':
                stack.append(0)
            else:
                x=stack.pop()
                stack[-1]+=max(2*x,1)
        
        return stack[0]