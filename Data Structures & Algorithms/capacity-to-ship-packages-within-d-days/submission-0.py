class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def capCheck(cap):
            ships = 1
            curCap = cap
            for w in weights:
                if curCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    curCap = cap
                curCap -= w
            return True
        res = r
        while l <= r:
            cap = (l + r) // 2
            if capCheck(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res