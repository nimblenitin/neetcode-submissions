class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        minH = []
        cache = {}
        for v in hand:
            cache[v] = 1 + cache.get(v, 0) 
        minH = list(cache.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in cache:
                    return False
                cache[i] -= 1
                if cache[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
