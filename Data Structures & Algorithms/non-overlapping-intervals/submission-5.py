class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[0])
        lastE = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if lastE > intervals[i][0]:
                res+= 1
                lastE = min(lastE, intervals[i][1])
            else:
                lastE = intervals[i][1]
                continue
        return res
