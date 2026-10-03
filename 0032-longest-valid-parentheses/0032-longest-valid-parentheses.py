class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        l=r=maxi=0
        for i in s:
            if i == '(':
                l+=1
            elif i==')':
                r+=1
            if l==r:
                maxi = max(l+r,maxi)
            if r>l:
                l=r=0
        l=r=0
        for i in range(n-1,-1,-1):
            if s[i] == '(':
                l+=1
            elif s[i]==')':
                r+=1
            if l==r:
                maxi = max(maxi,l+r)
            if l>r:
                l=r=0
        return maxi