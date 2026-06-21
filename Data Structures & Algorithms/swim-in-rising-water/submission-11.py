class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minH = [[grid[0][0], 0, 0]]
        N = len(grid)
        visit = set()
        visit.add((0, 0))

        while minH:
            t, r, c = heapq.heappop(minH)

            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if (nr < 0 or nc < 0 or nr == N or nc == N or
                    (nr, nc) in visit):
                    continue
                visit.add((nr, nc))
                heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])

            
