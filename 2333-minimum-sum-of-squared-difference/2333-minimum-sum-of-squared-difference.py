class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        max_val = 100000
        count = [0] * (max_val + 1)
        
        # Step 1: Count frequencies of absolute differences
        for a, b in zip(nums1, nums2):
            count[abs(a - b)] += 1
            
        # Total available operations
        K = k1 + k2
        
        # Step 2: Greedily reduce the largest differences
        for v in range(max_val, 0, -1):
            if count[v] > 0:
                take = min(K, count[v])
                K -= take
                count[v] -= take
                count[v - 1] += take
                
                if K == 0:
                    break
                    
        # Step 3: Calculate the minimum sum of squared differences
        ans = 0
        for v in range(max_val + 1):
            if count[v] > 0:
                ans += count[v] * (v * v)
                
        return ans