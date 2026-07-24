class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        strs.sort()
        l=len(strs[0])
        ans=''
        for i in range(l):
            if strs[0][i]!=strs[-1][i]:
                break
            ans+=strs[0][i]
        return ans

