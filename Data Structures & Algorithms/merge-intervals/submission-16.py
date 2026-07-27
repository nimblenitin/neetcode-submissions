class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for s, e in intervals:
            if res[-1][1] >= s:
                res[-1][1] = max(res[-1][1], e)
            
            else:
                res.append([s, e])
        return res
