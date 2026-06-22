class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
        n = len(points)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
            
        minH = [[0, 0]]
        visit = set()
        minCost = 0
        while len(visit) < n:
            dist1, n1 = heapq.heappop(minH)
            if n1 in visit:
                continue
            
            visit.add(n1)
            minCost += dist1

            for dist2, n2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minH, [dist2, n2])
        return minCost