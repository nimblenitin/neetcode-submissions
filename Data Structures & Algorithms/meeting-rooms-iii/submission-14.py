class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        used = []
        available = [i for i in range(n)]
        count = [0] * n

        for s, e in meetings:
            while used and s > used[0][0]:
                _, r = heapq.heappop(used)
                heapq.heappush(available, r)
            
            if not available:
                end, room = heapq.heappop(used)
                e = end + (e - s)
                heapq.heappush(available, room)
            
            aRoom = heapq.heappop(available)
            heapq.heappush(used, (e, aRoom))

            count[aRoom] += 1
        return count.index(max(count))