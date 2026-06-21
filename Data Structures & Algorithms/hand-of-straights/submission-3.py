class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = {}
        for v in hand:
            count[v] = count.get(v, 0) + 1
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, groupSize + first):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if minH[0] != i:
                        return False
                    heapq.heappop(minH)
        return True