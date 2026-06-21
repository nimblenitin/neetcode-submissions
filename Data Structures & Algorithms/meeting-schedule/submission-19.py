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
        prevE = intervals[0].end

        for interval in intervals[1:]:
            if prevE > interval.start:
                return False
            prevE = interval.end
        return True

        