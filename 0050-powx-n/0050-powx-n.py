class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==1 or x==0:
            return x
        if n==0:
            return 1
        if n==1:
            return x
        if n<0:
            x=1/x
            n=-n
        half = self.myPow(x,n//2)
        if n%2 ==0:
            return half*half
        else:
            return half*half*x
