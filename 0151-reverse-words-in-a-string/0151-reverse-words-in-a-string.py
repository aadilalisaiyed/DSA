class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        print(words)
        words.reverse()
        print(words)
        ans = " ".join(words)
        print(ans)
        return ans
