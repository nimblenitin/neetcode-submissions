class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            while q:
                r, c = q.popleft()
                if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                    grid[r][c] != "1" or ((r, c)) in visit):
                    continue
                visit.add((r, c))
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    bfs(nr, nc)
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    if (r, c) not in visit:
                        bfs(r, c)
                        res += 1
        return res
                    


                