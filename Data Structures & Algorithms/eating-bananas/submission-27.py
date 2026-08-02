class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = l = 1
        r = max(piles)

        while l <= r:
            m = (l + r) // 2
            totT = 0
            for p in piles:
                totT += math.ceil(p / m)
            if totT > h:
                l = m + 1
            else:
                r = m - 1
                res = m
        return res