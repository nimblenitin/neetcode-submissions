class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        angel = {}
        def dfs(r, c, prev):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or matrix[r][c] <= prev):
                return 0
            if (r, c) in angel:
                return angel[(r, c)]
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            angel[(r, c)] = res
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                 dfs(r, c, -1)
        return max(angel.values())