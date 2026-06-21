class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        i = 0
        minH = []
        qToI = {}
        for q in sorted(queries):
            while i < len(intervals) and q >= intervals[i][0]:
                l, r = intervals[i]
                heapq.heappush(minH, (r - l + 1, r))
                i += 1
            while minH and minH[0][1] < q:
                heapq.heappop(minH)
            qToI[q] = minH[0][0] if minH else -1
        return [qToI[q] for q in queries]
            


