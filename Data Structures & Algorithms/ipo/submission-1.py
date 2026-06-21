class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapital = [(minCap, maxP) for minCap, maxP in zip(capital, profits)]
        heapq.heapify(minCapital)
        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                curMinCap, curMaxP = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -curMaxP)
            if not maxProfit:
                break
            w += -heapq.heappop(maxProfit)
        return w
            
