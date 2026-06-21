class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfitHeap = []
        capitalHeap = [(cap, prof) for cap, prof in zip(capital, profits)]
        heapq.heapify(capitalHeap)
        count = 0
        for _ in range(k):
            while capitalHeap and capitalHeap[0][0] <= w:
                Curcap, curProf = heapq.heappop(capitalHeap)
                heapq.heappush(maxProfitHeap, -curProf)
            if not maxProfitHeap:
                break
            w += -heapq.heappop(maxProfitHeap)
        return w
            

            
