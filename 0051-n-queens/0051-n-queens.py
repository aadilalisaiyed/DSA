class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board = [["."] * n for _ in range(n)]
        print(board)
        hori_rows=set()
        diag1=set() 
        diag2=set() 
        def safe(col,row,board):
            if row in hori_rows or row-col in diag1 or row+col in diag2:
                return False
            return True
        def solve(col,board):
            if col == n:
                ans.append(["".join(r) for r in board])
                return
            for row in range(n):
                if safe(col,row,board):
                    board[row][col]="Q"
                    hori_rows.add(row)
                    diag1.add(row-col)
                    diag2.add(row+col)
                    solve(col+1,board)
                    board[row][col]="."
                    hori_rows.remove(row)
                    diag1.remove(row-col)
                    diag2.remove(row+col)
        solve(0,board)
        return ans