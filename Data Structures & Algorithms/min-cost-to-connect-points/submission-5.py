class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        minH = [[0, 0]]
        visit = set()
        totDist = 0
        while minH:
            mDist, node = heapq.heappop(minH)

            if node in visit:
                continue
            
            totDist += mDist
            
            visit.add(node)
            for dist2, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minH, [dist2, nei])
        
        return totDist
