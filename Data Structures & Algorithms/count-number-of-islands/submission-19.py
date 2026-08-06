class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        def bfs(r, c):
            count = 0
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))
            

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                        grid[nr][nc] != "1"):
                        continue
                    grid[nr][nc] = "0"
                    q.append((nr, nc))
            return count
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
        return res