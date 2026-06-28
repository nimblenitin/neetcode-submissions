class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            totT = 0
            for p in piles:
                totT += math.ceil(p / m)
            if totT <= h:
                r = m - 1
                res = m
            else: 
                l = m + 1 
        return res


        


        