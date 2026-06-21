class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-fr for fr in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        while q or maxHeap:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, (time + n)])
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

                
            