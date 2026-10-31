"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = sorted([i.start for i in intervals])
        e = sorted([j.end for j in intervals])
        si = ei = 0
        res = tmp = 0
        while si < len(s):
            if s[si] < e[ei]:
                tmp += 1
                si += 1
            else:
                tmp -= 1
                ei += 1
            res = max(res, tmp)
        return res