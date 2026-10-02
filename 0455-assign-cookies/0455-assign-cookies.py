class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        n=len(g)
        m=len(s)
        p1 =0
        p2=0
        ans=0
        while p1<n and p2<m:
            if s[p2]>=g[p1]:
                ans+=1
                p1+=1
            p2+=1
            
        return ans
            
            