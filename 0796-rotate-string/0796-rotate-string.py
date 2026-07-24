class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n=len(s)
        if len(s) != len(goal):
            return False
        for k in range(n):
            if goal == (s[k:] +s[:k]):
                return True
        return False
