class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        minHeap = []
        for value, freq in count.items():
            heapq.heappush(minHeap, (freq, value))
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        for i in range(k):
            if minHeap:
                res.append(heapq.heappop(minHeap)[1])
        return res
        