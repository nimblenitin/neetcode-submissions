"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = sorted([s.start for s in intervals])
        e = sorted([e.end for e in intervals])
        st = 0
        en = 0
        res = 0
        count = 0
        while st < len(intervals):
            if s[st] < e[en]:
                st += 1
                count += 1
            else:
                count -= 1
                en += 1
            res = max(res, count)
        return res


