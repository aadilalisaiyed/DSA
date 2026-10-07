class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        pocket=0
        c5=0
        c10=0
        for bill in bills:
            if bill == 10:
                if c5>0:
                    c5-=1
                    c10+=1
                else:
                    return False
            elif bill == 20:
                if c10>0 and c5>0:
                    c10-=1
                    c5-=1
                elif c5>2:
                    c5-=3
                else:
                    return False
            else:
                c5+=1
        return True
