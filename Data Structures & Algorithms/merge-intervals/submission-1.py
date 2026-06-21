class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]
        for start, end in intervals:
            lastE = res[-1][1]
            if lastE >= start:
                res[-1][1] = max(lastE, end)
            else:
                res.append([start, end])
        return res