class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)]
        used = []
        res = [0] * len(meetings)
        for s, e in meetings:
            while used and s >= used[0][0]:
                _, r = heapq.heappop(used)
                heapq.heappush(available, r)
            
            if not available and used:
                end, room = heapq.heappop(used)
                e = end + (e - s)
                heapq.heappush(available, room)
            rm = heapq.heappop(available)
            heapq.heappush(used, [e, rm])
            res[rm] += 1
        return res.index(max(res))