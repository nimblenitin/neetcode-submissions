class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxH = [-cnt for cnt in freq.values()]
        heapq.heapify(maxH)
        q = deque()
        time = 0
        while q or maxH:
            time += 1
            
            if maxH:
                curFreq = 1 + heapq.heappop(maxH)
                if curFreq:
                    q.append([time + n, curFreq])
            
            while q and q[0][0] == time:
                _, currFreq = q.popleft()
                heapq.heappush(maxH, currFreq)
        return time
            

            
            


