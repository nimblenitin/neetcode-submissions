class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreqHeap = [-count for count in freq.values()]
        heapq.heapify(maxFreqHeap)
        time = 0
        q = deque()
        while maxFreqHeap or q:
            if maxFreqHeap:
                curFreq = 1 + heapq.heappop(maxFreqHeap)
                if curFreq != 0:
                    q.append((time + n + 1, curFreq))
                time += 1
            else: 
                time = q[0][0]
            while q and time >= q[0][0]:
                _, freqNewEligible = q.popleft()
                heapq.heappush(maxFreqHeap, freqNewEligible)
        return time
            
            


