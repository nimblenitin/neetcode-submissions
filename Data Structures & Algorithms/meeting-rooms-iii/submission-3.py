class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]
        used = [] # endtime, room
        count = [0] * n
        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            
            if not available:
                curEnd, curRoom = heapq.heappop(used)
                end = curEnd + (end - start)
                heapq.heappush(available, curRoom)

            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1
        return count.index(max(count))

