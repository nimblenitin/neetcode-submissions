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
        tot = cur = 0

        while si < len(intervals):
            if s[si] < e[ei]:
                cur += 1
                si += 1
            else:
                cur -= 1
                ei += 1
            tot = max(cur, tot)
        return tot 


        
        
