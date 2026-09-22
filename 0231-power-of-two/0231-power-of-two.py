class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        s=""
        while n>0:
            if n%2==1:
                s='1'+s[:]
            else:
                s='0'+s[:]
            n//=2
        c=0
        for i in s:
            if i=='1':
                c+=1
        
        return c==1