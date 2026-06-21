class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def makeoTBorder(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                makeoTBorder(nr, nc)

        for r in range(ROWS):
            makeoTBorder(r, 0)
            makeoTBorder(r, COLS - 1)

        for c in range(COLS):
            makeoTBorder(0, c)
            makeoTBorder(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"
