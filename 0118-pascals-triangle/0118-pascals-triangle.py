class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[]
        for i in range(numRows):
            triangle.append([])
        print(triangle)
        if numRows == 0:
            return 0
        triangle[0].append(1)
        for i in range(1,numRows):
            triangle[i].append(1)
            for j in range(i-1):
                triangle[i].append(triangle[i-1][j]+triangle[i-1][j+1])
            triangle[i].append(1) 
        
        return triangle
