class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        mHeap = [(0, k)]
        visit = set()
        t = 0
        while mHeap:
            w1, n1 = heapq.heappop(mHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            for nei, w2 in adj[n1]:
                if nei not in visit:
                    heapq.heappush(mHeap, (w1 + w2, nei))
        return t if len(visit) == n else -1

        
        