class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        def valid(cap):
            curC = cap
            ships = 1
            for w in weights:
                if curC - w < 0:
                    ships += 1
                    curC = cap
                    if ships > days:
                        return False
                curC -= w
            return True
        res = sum(weights)
        while l <= r:
            cap = (l + r) // 2
            if valid(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res

        
