class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        def helper(idx,i,j):
            if idx==len(word):
                return True
            if  i<0 or j<0 or i>=m or j>=n or word[idx]!=board[i][j]:
                return False
            temp = board[i][j]
            board[i][j] = "#"  #To avoid revisiting same node again
            left = helper(idx+1,i,j-1)
            top = helper(idx+1,i-1,j)
            right = helper(idx+1,i,j+1)
            bottom = helper(idx+1,i+1,j)

            board[i][j] = temp

            return left or top or right or bottom
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and helper(0,i,j):
                    return True
        return False
        

        