class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for n1, n2, w1 in times:
            adj[n1].append((n2, w1))
        mHeap = [(0, k)]
        res = 0
        visit = set()
        while mHeap:
            w1, n1 = heapq.heappop(mHeap)
            if n1 in visit:
                continue
            res = w1
            visit.add(n1)
            for n2, w2 in adj[n1]:
                heapq.heappush(mHeap, (w1 + w2, n2))
        return res if len(visit) == n else -1


        
        