class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board = [["."] * n for _ in range(n)]
        print(board)
        def safe(col,row,board):
            r,c=row,col
            while row>=0 and col>=0:
                if board[row][col]=='Q':
                    return False
                row-=1
                col-=1
            row,col=r,c

            while row<n and col>=0:
                if board[row][col]=='Q':
                    return False
                row+=1
                col-=1

            row,col=r,c
            while col>=0:
                if board[row][col]=='Q':
                    return False
                col-=1
            return True
        def solve(col,board):
            if col == n:
                ans.append(["".join(r) for r in board])
                return
            for row in range(n):
                if safe(col,row,board):
                    board[row][col]="Q"
                    solve(col+1,board)
                    board[row][col]="."
        solve(0,board)
        return ans