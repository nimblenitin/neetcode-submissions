class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxH = [-f for _, f in freq.items()]
        heapq.heapify(maxH)
        q = deque()
        time = 0
        while maxH or q:
            time += 1
            while q and q[0][1] == time:
                frequ, tim = q.popleft()
                heapq.heappush(maxH, frequ)
            if maxH:
                fre = heapq.heappop(maxH)
                fre = 1 + fre
                if fre != 0:
                    q.append([fre, time + n + 1])
            
            
        return time            


