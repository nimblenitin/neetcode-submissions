class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [False] * n
        res = 0
        
        for num in range(2, n):
            if not sieve[num]:
                for j in range(num * num, n, num):
                    sieve[j] = True
                res += 1
        return res        