class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def makeT(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                board[r][c] != "O"):
                return

            board[r][c] = "T"
            makeT(r + 1, c)
            makeT(r - 1, c)
            makeT(r, c + 1)
            makeT(r, c - 1)

        for r in range(ROWS):
            makeT(r, 0)
            makeT(r, COLS - 1)

        for c in range(COLS):
            makeT(0, c)
            makeT(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


        