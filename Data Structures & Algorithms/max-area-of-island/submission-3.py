class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or
                grid[r][c] == 0):
                return 0
            visit.add((r, c))
            maxA = 1
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                maxA += dfs(nr, nc)
            return maxA

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea


            
