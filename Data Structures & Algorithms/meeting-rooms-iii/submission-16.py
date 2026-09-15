class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        count = [0] * n

        available = [i for i in range(n)]
        used = [] # (endT, R)

        for s, e in meetings:
            while used and s > used[0][0]:
                _, r = heapq.heappop(used)
                heapq.heappush(available, r)
            
            if not available:
                endT, ro = heapq.heappop(used)
                curLen = e -  s
                s = endT
                e = endT + curLen
                heapq.heappush(available, ro)
            
            aR = heapq.heappop(available)
            heapq.heappush(used, (e, aR))
            count[aR] += 1
        return count.index(max(count))
            
            



                


            