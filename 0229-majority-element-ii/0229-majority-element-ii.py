class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {} # key = elt : value = freq
        ans = []
        n = len(nums)
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        print(freq)
        l = len(freq)
        
        for i,k in enumerate(freq):
            if freq[k] > n//3:
                ans.append(k)
        return ans