class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k + 1):
            priceC = prices.copy()
            for s, d, p in flights:
                if priceC[s] == float("inf"):
                    continue
                if priceC[d] > p + prices[s]:
                    priceC[d] = p + prices[s]
            prices = priceC
        return -1 if prices[dst] == float("inf") else prices[dst]

