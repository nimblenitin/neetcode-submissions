class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = pow(x * x, n // 2)
            return res if n % 2 == 0 else res * x

        output = pow(x, abs(n))
        return output if n >= 0 else 1 / output
