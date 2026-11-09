class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxH = [-f for k, f in freq.items()]
        heapq.heapify(maxH)
        q = deque()
        time = 0
        while q or maxH:
            time += 1
            while q and q[0][0] == time:
                _, fr = q.popleft()
                heapq.heappush(maxH, fr)
            
            if maxH:
                nF = 1 + heapq.heappop(maxH)
                if nF:
                    q.append((time + n + 1, nF))
        return time


        
