class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ans=[]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    x = board[i][j]
                    box = (i // 3) * 3 + (j // 3)

                    rows[i].add(x)
                    cols[j].add(x)
                    boxes[box].add(x)

        def helper(i,j):
            if i==9:
                return True
            if j==9:
                return helper(i+1,0)
            if board[i][j] != '.':
                return helper(i, j + 1)
            
            box = (i // 3) * 3 + (j // 3)

            for x in "123456789":

                if (x not in rows[i] and
                    x not in cols[j] and
                    x not in boxes[box]):

                    # Choose
                    board[i][j] = x
                    rows[i].add(x)
                    cols[j].add(x)
                    boxes[box].add(x)

                    # Explore
                    if helper(i, j + 1):
                        return True

                    # Undo
                    board[i][j] = '.'
                    rows[i].remove(x)
                    cols[j].remove(x)
                    boxes[box].remove(x)

            return False

        helper(0, 0)
                    



        