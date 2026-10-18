class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        topK = [[] for _ in range(len(nums) + 1)]

        for v, f in freq.items():
            topK[f].append(v)
        res = []
        for i in range(len(topK) - 1, -1, -1):
            for val in topK[i]:
                res.append(val)
                if len(res) == k:
                    return res