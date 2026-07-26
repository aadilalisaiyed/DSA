class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        n=len(s)
        mp={}
        for i in s:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        for i in t:
            if i in mp:
                mp[i]-=1
            else:
                mp[i]=-1
            if mp[i]==0:
                mp.pop(i)
        if mp == {}:
            return True
        return False
        
        