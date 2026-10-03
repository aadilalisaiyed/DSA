class Solution:
    def divide(self, dividend: int, divisor: int) -> int: #d/n
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        # Handling Signs
        sign = False
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            sign = True
        n=abs(dividend)
        d=abs(divisor)
        # Applying logic
        res=0
        while n>=d:
            c=0
            while n>=(d<<(c+1)):
                c+=1
            n-=(d<<c)
            res+=(1<<c)
        if sign:
            res=-res
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return max(INT_MIN,min(INT_MAX,res))

