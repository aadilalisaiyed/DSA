class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        n=len(s)
        ans=0
        p=0
        for i in range(n-1,-1,-1):
            if s[i]=='I':
                if p > 1:
                    ans-=1
                else:
                    ans+=1
                p=max(p,1)
            elif s[i]=='V':
                if p > 2:
                    ans-=5
                else:
                    ans+=5
                p=max(p,2)
            elif s[i]=='X':
                if p > 3:
                    ans-=10
                else:
                    ans+=10
                p=max(p,3)
            elif s[i]=='L':
                if p > 4:
                    ans-=50
                else:
                    ans+=50
                p=max(p,4)
            elif s[i]=='C':
                if p > 5:
                    ans-=100
                else:
                    ans+=100
                p=max(p,5)
            elif s[i]=='D':
                if p > 6:
                    ans-=500
                else:
                    ans+=500
                p=max(p,6)
            elif s[i]=='M':
                if p > 7:
                    ans-=1000
                else:
                    ans+=1000
                p=max(p,7)
        return ans



