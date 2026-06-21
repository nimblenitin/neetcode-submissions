class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        i = 0
        qToI = {}
        minH = []
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minH, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while minH and minH[0][1] < q:
                heapq.heappop(minH)
            qToI[q] = minH[0][0] if minH else -1
        return [qToI[qu] for qu in queries]




        