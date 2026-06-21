class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)
        
        def capValid(cap):
            curCap = cap
            ship = 1
            for w in weights:
                if curCap - w < 0:
                    ship += 1
                    curCap = cap
                    if ship > days:
                        return False
                curCap -= w
            return True

        res = r
        while l <= r:
            cap = (l + r) // 2
            if capValid(cap):
                r = cap - 1
                res = cap
            else:
                l = cap + 1
        return res
