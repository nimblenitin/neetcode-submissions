class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(cap):
            curCap = cap
            ships = 1
            for w in weights:
                curCap -= w
                if curCap < 0:
                    ships += 1
                    curCap = cap - w
                if ships > days:
                    return False
                
            return True

        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            cap = (l + r) // 2
            if valid(cap):
                res = min(cap, res)
                r = cap - 1
            else:
                l = cap + 1
        return res

        