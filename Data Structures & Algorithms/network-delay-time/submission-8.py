class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))
        
        minH = []
        minH.append([0, k])
        visit = set()
        minT = 0
        while minH:
            t, n1 = heapq.heappop(minH)
            if n1 in visit:
                continue
            visit.add(n1)
            minT = max(minT, t)
            for n2, t2 in adj[n1]:
                heapq.heappush(minH, [t + t2, n2])
                
        return minT if len(visit) == n else -1

