class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevE = intervals[0][1]
        count = 0
        for start, end in intervals[1:]:
            
            if prevE <= start:
                prevE = end
            else:
                count += 1
                prevE = min(prevE, end)
        return count
                
        