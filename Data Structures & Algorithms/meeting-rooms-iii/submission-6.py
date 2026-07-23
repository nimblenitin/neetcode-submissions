class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)]
        used = []
        freq = [0] * n

        for start, end in meetings:
            while used and start >= used[0][0]:
                _, r = heapq.heappop(used)
                heapq.heappush(available, r)
            
            if not available:
                e, ro = heapq.heappop(used)
                end = (end - start) + e
                heapq.heappush(available, ro)
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            freq[room] += 1
        return freq.index(max(freq))          
                    