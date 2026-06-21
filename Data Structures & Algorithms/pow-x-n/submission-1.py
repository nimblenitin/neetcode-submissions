class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = helper(x * x, abs(n) // 2)
            return res if n % 2 == 0 else x * res
        
        res = helper(x, n)
        return res if n >= 0 else 1 / res

