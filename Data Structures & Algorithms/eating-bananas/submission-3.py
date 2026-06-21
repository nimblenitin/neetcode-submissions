class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            curTotHours = 0
            for p in piles:
                curTotHours += math.ceil(float(p) / m)
            if curTotHours <= h:
                r = m - 1
                res = m
            else:
                l = m + 1
        return res  
