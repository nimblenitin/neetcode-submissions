class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n = self.sON(n)
        return False

    def sON(self, n):
        output = 0
        while n:
            digit = n % 10
            output += digit ** 2
            n = n // 10
        return output