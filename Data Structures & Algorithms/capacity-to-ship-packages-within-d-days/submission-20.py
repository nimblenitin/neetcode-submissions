class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        res = sum(weights)

        def isVal(cap):
            curC = cap
            ships = 1
            for w in weights:
                if curC - w < 0:
                    curC = cap
                    ships += 1
                    if ships > days:
                        return False
                curC -= w
            return True

        while l <= r:
            m = (l + r) // 2

            if isVal(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res