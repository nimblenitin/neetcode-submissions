class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            curH = 0
            for p in piles:
                curH += math.ceil(p / m)
            if curH <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        return res