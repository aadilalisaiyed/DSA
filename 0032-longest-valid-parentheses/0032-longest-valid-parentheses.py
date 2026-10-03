class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l=r=maxi=0
        for i in s:
            if i == '(':
                l+=1
            else:
                r+=1
            if l==r:
                maxi = max(l+r,maxi)
            elif r>l:
                l=r=0
        l=r=0
        for i in reversed(s):
            if i == '(':
                l+=1
            else:
                r+=1
            if l==r:
                maxi = max(maxi,l+r)
            elif l>r:
                l=r=0
        return maxi