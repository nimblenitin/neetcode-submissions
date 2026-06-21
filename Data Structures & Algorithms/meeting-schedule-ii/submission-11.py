"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sSorted = sorted([i.start for i in intervals])
        eSorted = sorted([i.end for i in intervals])

        start = 0
        end = 0
        curMax = 0
        totMax = 0
        while start < len(sSorted):
            if sSorted[start] < eSorted[end]:
                curMax += 1
                totMax = max(curMax, totMax)
                start += 1
            else:
                curMax -= 1
                end += 1
        return totMax