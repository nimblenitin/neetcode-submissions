class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = sum(weights)

        def isVal(cap):
            curC = cap
            ships = 1
            for w in weights:
                if curC - w < 0:
                    ships += 1
                    curC = cap
                curC -= w
                if ships > days:
                    return False
            return True
 
        while l <= r:
            m = (l + r) // 2
            if isVal(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res