"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if not intervals:
            return True
        prevEnd = intervals[0].end
        for intr in intervals[1:]:
            if prevEnd > intr.start:
                return False
            prevEnd = intr.end
        return True