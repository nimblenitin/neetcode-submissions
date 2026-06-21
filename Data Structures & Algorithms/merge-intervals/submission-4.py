class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if output[-1][1] >= start:
                output[-1][1] = max(end, output[-1][1])
            else:
                output.append([start, end])
        return output