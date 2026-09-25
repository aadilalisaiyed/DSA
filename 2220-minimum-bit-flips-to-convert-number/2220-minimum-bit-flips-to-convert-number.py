class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x=start^goal
        c=0
        while x>0:
            if x&1:
                c+=1
            x>>=1
        return c