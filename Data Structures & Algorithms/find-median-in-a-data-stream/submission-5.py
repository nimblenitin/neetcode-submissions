class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
    def addNum(self, num: int) -> None:
        if self.large and num < self.large[0]:
            heapq.heappush(self.small, -1 * num)
        else:
            heapq.heappush(self.large, num)
        if len(self.small) > len(self.large) + 1:
            smlVal = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * smlVal)
        elif len(self.small) + 1 < len(self.large):
            larVal = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * larVal)
        else:
            return

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]        
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2.0

        
        