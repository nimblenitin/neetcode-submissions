class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                maxP = prices[r] - prices[l]
                profit = max(profit, maxP)
            else:
                l = r
            r += 1
        return profit             