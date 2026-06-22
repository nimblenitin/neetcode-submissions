class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minH = [[grid[0][0], 0, 0]]
        visit = set()
        visit.add((0, 0))
        ROWS = len(grid)
        maxT = 0
        COLS = len(grid[0])

        while minH:
            t, r, c = heapq.heappop(minH)
            maxT = max(t, maxT)
            if r == ROWS - 1 and c == COLS - 1:
                return maxT

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or 
                    (nr, nc) in visit):
                    continue
                visit.add((nr, nc))
                heapq.heappush(minH, [max(grid[nr][nc], t), nr, nc])

            
