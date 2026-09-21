"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        tot = 0
        s = sorted([i.start for i in intervals])
        e = sorted([j.end for j in intervals])
        sI, eI = 0, 0
        tmp = 0
        while sI < len(s):
            if s[sI] < e[eI]:
                tmp += 1
                sI += 1
            else:
                tmp -= 1
                eI += 1
            tot = max(tot, tmp)
        return tot