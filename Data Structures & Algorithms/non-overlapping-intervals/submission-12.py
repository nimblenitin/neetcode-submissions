class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        tot = 0
        prevE = intervals[0][1]

        for i in range(1, len(intervals)):
            if prevE > intervals[i][0]:
                tot += 1
                prevE = min(prevE, intervals[i][1])
            else:
                prevE = intervals[i][1]
        return tot