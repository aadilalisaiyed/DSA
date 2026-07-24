class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1={}
        n=len(s)
        for i in range(n):
            if s[i] in map1:
                if t[i] != map1[s[i]]:
                    return False
            map1[s[i]]=t[i]
        map2={}
        n=len(t)
        for i in range(n):
            if t[i] in map2:
                if s[i] != map2[t[i]]:
                    return False
            map2[t[i]]=s[i]
        return True