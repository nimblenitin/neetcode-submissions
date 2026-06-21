class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visit = set()
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            while q:
                r, c = q.popleft()
                visit.add((r, c))
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if not (nr >= ROWS or nc >= COLS or nr < 0 or nc < 0 or (nr, nc) in visit or
                            grid[nr][nc] == "0"):
                        q.append((nr, nc))
                    

                    
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    if (r, c) not in visit:
                        res += 1
                        bfs(r, c)
        return res
                