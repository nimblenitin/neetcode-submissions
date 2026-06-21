# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n = n
        celebrity_candidate = 0
        for i in range(1, n):
            if knows(celebrity_candidate, i):
                celebrity_candidate = i
        if self.isCelebrity(celebrity_candidate):
            return celebrity_candidate
        return -1
    
    def isCelebrity(self, candidate):
        for j in range(self.n):
            if j == candidate:
                continue
            if knows(candidate, j) or not knows(j, candidate):
                return False
        return True
            