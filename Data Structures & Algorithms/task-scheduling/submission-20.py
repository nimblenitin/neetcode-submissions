class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxH = [-v for k, v in freq.items()]
        heapq.heapify(maxH)
        q = deque()
        time = 0
        while maxH or q:
            time += 1
            while q and q[0][0] == time:
                _, f = q.popleft()
                heapq.heappush(maxH, f)
            
            if maxH:
                f = heapq.heappop(maxH)
                f = 1 + f
                if f:
                    q.append([time + n + 1, f])
        return time