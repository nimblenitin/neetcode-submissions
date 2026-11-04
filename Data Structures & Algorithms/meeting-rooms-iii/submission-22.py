class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        count = [0] * n
        used = []
        available = [i for i in range(n)]
        for s, e in meetings:   
            while used and used[0][0] <= s:
                _, r = heapq.heappop(used)
                heapq.heappush(available, r)
            
            if not available:
                end, ro = heapq.heappop(used)
                cL = e - s
                e = end + cL
                heapq.heappush(available, ro)
            room = heapq.heappop(available)
            heapq.heappush(used, (e, room))
            count[room] += 1
        return count.index(max(count))



        