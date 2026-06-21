class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapital = [(capital, profit) for capital, profit in zip(capital, profits)]
        heapq.heapify(minCapital)
        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                curCapital, curProfit = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -curProfit)
            
            if not maxProfit:
                break
            w += -heapq.heappop(maxProfit)
        return w

            
