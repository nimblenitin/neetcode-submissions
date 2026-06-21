class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        while q or maxHeap:
            if maxHeap:
                curFreq = 1 + heapq.heappop(maxHeap)
                time += 1
                if curFreq:
                    q.append((time + n, curFreq))
            else:
                time = q[0][0]
            while q and time >= q[0][0]:
                _, qFreq = q.popleft()
                heapq.heappush(maxHeap, qFreq)
        return time
                 
            
            


