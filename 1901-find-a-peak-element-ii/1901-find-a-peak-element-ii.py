class Solution:
    def maxIdx(self,arr):
        ans=-1
        idx=-1
        for i in range(len(arr)):
            if arr[i]>ans:
                ans=arr[i]
                idx=i
        return idx
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        l,r=0,n-1
        while l<=r:
            mid = (l+r)//2
            maxidx = self.maxIdx(mat[mid])
            top = mat[mid-1][maxidx] if mid>0 else -1
            bottom = mat[mid+1][maxidx] if mid < n-1 else -1
            if bottom<mat[mid][maxidx]>top:
                return (mid,maxidx)
            elif bottom>mat[mid][maxidx]:
                l=mid+1
            else:
                r=mid-1
        return [-1,-1]