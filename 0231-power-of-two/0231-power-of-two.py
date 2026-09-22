class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        s=""
        c=0
        while n>0:
            if n%2==1:
                s='1'+s[:]
                c+=1
            else:
                s='0'+s[:]
            n//=2
        
        
        return c==1