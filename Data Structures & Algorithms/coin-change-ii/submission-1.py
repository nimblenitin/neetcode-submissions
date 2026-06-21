class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nDp = [0] * (amount + 1)
            nDp[0] = 1
            for a in range(1, amount + 1):
                nDp[a] = dp[a]
                if a - coins[i] >= 0:
                    nDp[a] += nDp[a - coins[i]]
            dp = nDp
        return dp[amount]

             