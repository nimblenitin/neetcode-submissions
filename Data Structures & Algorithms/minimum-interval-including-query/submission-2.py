class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minH = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                    l, r = intervals[i]
                    heapq.heappush(minH, (r - l + 1, r))
                    i += 1
            while minH and minH[0][1] < q:
                heapq.heappop(minH)
            res[q] = minH[0][0] if minH else -1
        return [res[q] for q in queries]