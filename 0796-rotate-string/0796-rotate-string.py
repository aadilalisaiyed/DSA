class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n=len(s)
        if len(s) != len(goal):
            return False
        x=s+s
        if goal in x:
            return True
        return False
