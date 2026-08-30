class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10**9 +7)
        def binexp(a,b):
            #to find a^b
            res=1
            a%=MOD
            while b>0:
                if b%2 == 1:
                    res = (res*a)%MOD
                a*=a%MOD
                b//=2
            return res%(10**9 +7)
        if n%2==0:
            return (binexp(5,n//2) * binexp(4,n//2))%MOD
        else:
            return (binexp(5,(n//2)+1) * binexp(4,n//2))%MOD
