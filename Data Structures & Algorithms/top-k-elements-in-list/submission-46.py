class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        topK = [[] for i in range(len(nums) + 1)]

        for num, v in freq.items():
            topK[v].append(num)
        res = []
        for i in range(len(nums), -1, -1):
            for val in topK[i]:
                res.append(val)
                if len(res) == k:
                    return res