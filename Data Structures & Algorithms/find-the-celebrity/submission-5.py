# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n = n
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        if self.checkCelebrity(candidate):
            return candidate
        return -1

    def checkCelebrity(self, celebrity):
        for i in range(self.n):
            if celebrity == i:
                continue
            if knows(celebrity, i) or not knows(i, celebrity):
                return False
        return True
            