class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def capValid(cap):
            ships= 1
            curCap = cap
            for w in weights:
                if curCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    curCap = cap
                curCap -= w
            return True
        l, r = max(weights), sum(weights)
        cap = r
        while l <= r:
            cap = (l + r) // 2
            if capValid(cap):
                r = cap - 1
                res = cap
            else:
                l = cap + 1
        return res
        
