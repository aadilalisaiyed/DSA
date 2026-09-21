class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        rowIndex+=1
        triangle=[]
        for i in range(rowIndex):
            triangle.append([])
        if rowIndex == 0:
            return 0
        triangle[0].append(1)
        for i in range(1,rowIndex):
            triangle[i].append(1)
            for j in range(i-1):
                triangle[i].append(triangle[i-1][j]+triangle[i-1][j+1])
            triangle[i].append(1) 
        
        return triangle[-1]
