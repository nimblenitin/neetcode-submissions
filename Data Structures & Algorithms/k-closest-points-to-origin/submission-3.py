class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minH = []
        for x1, y1 in points:
            dist = x1 ** 2 + y1 ** 2
            heapq.heappush(minH, [dist, x1, y1])
        heapq.heapify(minH)
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minH)
            res.append([x, y])
            k -= 1
        return res