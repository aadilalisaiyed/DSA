class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        l=len(s)
        for i in range(l):
            ans += (26-(ord(s[i])-ord('a')))*(i+1)
        return ans