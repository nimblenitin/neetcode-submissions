class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        for n in hand:
            count[n] = count.get(n, 0) + 1
        
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for v in range(first, first + groupSize):
                if v not in count:
                    return False
                count[v] -= 1
                if count[v] == 0:
                    if minH[0] != v:
                        return False
                    heapq.heappop(minH)
        return True
                    