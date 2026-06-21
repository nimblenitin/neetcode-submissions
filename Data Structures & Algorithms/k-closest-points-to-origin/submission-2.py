class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minH = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minH.append([dist, x, y])
        heapq.heapify(minH)
        res = []
        while k > 0:
            distance, x1, y1 = heapq.heappop(minH)
            k -= 1
            res.append([x1, y1])
        return res