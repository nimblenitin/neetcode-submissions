class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        used = []
        count = [0] * n
        available = [i for i in range(n)]

        for s, e in meetings:
            while used and used[0][0] < s:
                _, ro = heapq.heappop(used)
                heapq.heappush(available, ro)
            
            if not available:
                en, room = heapq.heappop(used)
                le = e - s
                e = en + le
                heapq.heappush(available, room)
            
            r = heapq.heappop(available)
            heapq.heappush(used, [e, r])
            count[r] += 1
        return count.index(max(count))