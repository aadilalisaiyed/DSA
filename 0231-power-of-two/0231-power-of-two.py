class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c=0
        while n>0:
            if n%2==1:
                c+=1
            n//=2
        return c==1