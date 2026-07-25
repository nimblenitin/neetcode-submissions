class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCap = [(cap, prof) for prof, cap in zip(profits, capital)]
        heapq.heapify(minCap)
        maxP = []

        for i in range(k):
            while minCap and minCap[0][0] <= w:
                c, p = heapq.heappop(minCap)
                heapq.heappush(maxP, -p)
            
            if not maxP:
                break
            
            w += -heapq.heappop(maxP)
        return w
