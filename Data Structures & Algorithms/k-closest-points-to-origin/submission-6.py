class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minH = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minH.append([dist, x, y])            
        
        heapq.heapify(minH)
        res = []
        while k > 0:
            _, x, y = heapq.heappop(minH)
            res.append([x, y])
            k -= 1
        return res