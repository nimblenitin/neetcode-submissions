class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minH = [[grid[0][0], 0, 0]]
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        maxT = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while minH:
            t, r, c = heapq.heappop(minH)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if r == ROWS - 1 and c == COLS - 1:
                return t
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or 
                    (nr, nc) in visit):
                    continue
                heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])
                
            

