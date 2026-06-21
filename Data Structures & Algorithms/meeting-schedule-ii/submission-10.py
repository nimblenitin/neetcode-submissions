"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = sorted([st.start for st in intervals])
        e = sorted([en.end for en in intervals])
        sta = 0
        curE = 0
        curMax = 0
        totMax = 0
        while sta < len(s):
            if s[sta] < e[curE]:
                curMax += 1
                totMax = max(curMax, totMax)
                sta += 1
            else:
                curE += 1
                curMax -= 1
        return totMax
            


