class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))

        minH = [(0, k)]
        visit = set()
        totTime = 0
        while minH:
            t1, n1 = heapq.heappop(minH)
            if n1 in visit:
                continue
            visit.add(n1)
            totTime = max(totTime, t1)
            for n2, t2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minH, (t1 + t2, n2))
        return totTime if len(visit) == n else -1


        