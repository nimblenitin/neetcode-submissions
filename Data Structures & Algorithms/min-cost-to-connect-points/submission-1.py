class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i: [] for i in range(len(points))}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i, len(points)):
                x2, y2 = points[j]
                w1 = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((w1, j))
                adj[j].append((w1, i))
        
        mHeap = [[0, 0]]
        visit = set()
        dist = 0
        while len(visit) < len(points):
            w1, n1 = heapq.heappop(mHeap)
            if n1 in visit:
                continue
            dist += w1
            visit.add(n1)
            for w2, nei in adj[n1]:
                if nei not in visit:
                    heapq.heappush(mHeap, ((w2, nei)))
        return dist
        
