class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # dp[i] = maximum palindromes we can get
        # from s[i:]
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):

            # Don't use s[i]
            dp[i] = dp[i + 1]

            # Try to find a palindrome starting at i
            for j in range(i + k - 1, n):

                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1

                if l >= r:
                    dp[i] = max(dp[i], 1 + dp[j + 1])
                    break

        return dp[0]