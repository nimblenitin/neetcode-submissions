class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair: pair[0])
        lastE = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < lastE:
                count += 1
                lastE = min(lastE, intervals[i][1])
            else:
                lastE = intervals[i][1]
        return count