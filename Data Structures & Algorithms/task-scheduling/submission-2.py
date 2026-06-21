class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-freq for freq in count.values()]
        heapq.heapify(maxHeap)
        q = deque() #time, curFreq
        time = 0
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][0]
            else:
                curFreq = 1 + heapq.heappop(maxHeap)
                if curFreq:
                    q.append(((time + n), curFreq))
            
            while q and time == q[0][0]:
                heapq.heappush(maxHeap, q.popleft()[1])
        return time
