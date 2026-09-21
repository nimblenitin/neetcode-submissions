class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0

        for s, e in intervals[1:]:
            if prevEnd > s:
                res += 1
                prevEnd = min(e, prevEnd)
            else:
                prevEnd = e
        return res