class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        n=len(g)
        m=len(s)
        i=j=0
        content=0
        while i<n and j<m:
            if s[j]>=g[i]:
                content+=1
                i+=1
            j+=1
        return content