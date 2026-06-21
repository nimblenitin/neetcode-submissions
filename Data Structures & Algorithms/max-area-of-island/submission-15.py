class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c):
            if (r, c) in visit or grid[r][c] == 0:
                return 0
            areaa = 0
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visit or grid[nr][nc] == 0):
                    continue
                
                areaa += dfs(nr, nc)
                
            return 1 + areaa
        maxA = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxA = max(maxA, dfs(r, c))
        return maxA
