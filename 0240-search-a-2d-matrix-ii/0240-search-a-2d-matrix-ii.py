class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        row=0
        col = m-1
        while row<=n-1 and col >= 0:
            curr=matrix[row][col]
            if curr == target:
                return True
            elif curr<target:
                row+=1
            else:
                col-=1
        return False
