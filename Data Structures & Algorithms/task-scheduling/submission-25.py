class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxH = [-v for k, v in freq.items()]
        heapq.heapify(maxH)
        time = 0 
        q = deque()

        while q or maxH:
            time += 1

            while q and q[0][0] == time:
                _, fr = q.popleft()
                heapq.heappush(maxH, fr)
            
            if maxH:
                cF = 1 + heapq.heappop(maxH)

                if cF:
                    q.append([time + n + 1, cF])
        return time




