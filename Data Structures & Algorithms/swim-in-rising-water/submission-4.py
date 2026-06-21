class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minH = [(grid[0][0], 0, 0)]
        visit = set()
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == len(grid) - 1 and c == len(grid[1]) - 1:
                return t
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0])):
                    continue
                if (nr, nc) not in visit:
                    heapq.heappush(minH, (max(t, grid[nr][nc]), nr, nc))

