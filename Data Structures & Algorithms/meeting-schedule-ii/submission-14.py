"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sSorted = sorted([s.start for s in intervals])
        eSorted = sorted(e.end for e in intervals)
        s = e = 0
        tot = curTot = 0
        while s < len(intervals):
            if sSorted[s] < eSorted[e]:
                curTot += 1
                tot = max(tot, curTot)
                s += 1
            else:
                e += 1
                curTot -= 1
        return tot
