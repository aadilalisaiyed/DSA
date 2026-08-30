class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10**9 +7)
        def binexp(a,b):
            #to find a^b
            if b==0:
                return 1
            res = binexp(a,b//2)
            if b%2:
                return (res*res*a)%MOD
            else:
                return (res*res)%MOD
        if n%2==0:
            return (binexp(5,n//2) * binexp(4,n//2))%MOD
        else:
            return (binexp(5,(n//2)+1) * binexp(4,n//2))%MOD
