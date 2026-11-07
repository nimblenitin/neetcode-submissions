class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minH = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minH)
        maxH = []
        for i in range(k):
            while minH and minH[0][0] <= w:
                cap, pro = heapq.heappop(minH)
                heapq.heappush(maxH, -pro)
            
            if not maxH:
                return w
            w += -heapq.heappop(maxH)
        return w


        