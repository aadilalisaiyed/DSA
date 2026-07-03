class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []
        # m is no. of rows
        # n is no. of columns
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)
        print(row,col)
        for i in range(len(row)):
            for j in range(m): #when we detect row, we modify column
                matrix[row[i]][j]=0
        for i in range(len(col)):
            for j in range(n): #when we detect col, we modify row
                matrix[j][col[i]]=0