class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCap = [(cap, prof) for cap, prof in zip(capital, profits)]
        heapq.heapify(minCap)
        maxP = []

        for i in range(k):
            while minCap and minCap[0][0] <= w:
                c, p = heapq.heappop(minCap)
                heapq.heappush(maxP, -p)
            
            if not maxP:
                return w
            
            w += -heapq.heappop(maxP)
        return w
        