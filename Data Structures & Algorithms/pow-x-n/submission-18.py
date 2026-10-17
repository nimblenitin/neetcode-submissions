class Solution:
    def myPow(self, x: float, n: int) -> float:
        def cal(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = cal(x, n // 2)
            res *= res 

            return res if n % 2 == 0 else res * x
        
        aRes = cal(x, abs(n))
        return aRes if n >= 0 else 1 / aRes


        