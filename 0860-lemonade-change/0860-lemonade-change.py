class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        pocket=0
        c5=0
        c10=0
        for bill in bills:
            if c5<0 or c10<0:
                return False
            if bill == 10:
                c10+=1
                c5-=1
            elif bill == 20:
                if c10>0:
                    c10-=1
                else:
                    c5-=2
                c5-=1
            else:
                c5+=1
    
        if c5<0 or c10<0:
            return False
        else:
            return True
