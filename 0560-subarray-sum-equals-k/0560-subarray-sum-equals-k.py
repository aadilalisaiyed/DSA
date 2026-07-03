class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        ans = 0
        seen = {0: 1}

        for num in nums:
            prefix += num

            if prefix - k in seen:
                ans += seen[prefix - k]

            if prefix in seen:
                seen[prefix] += 1
            else:
                seen[prefix] = 1

        return ans