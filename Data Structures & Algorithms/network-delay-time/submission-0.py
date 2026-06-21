class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for n1, n2, t in times:
            edges[n1].append((t, n2))
        
        visit = set()
        minHeap = [(0, k)]
  
        t = 0
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = t1
            for t2, n2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (t1 + t2, n2))
        return t if len(visit) == n else -1



