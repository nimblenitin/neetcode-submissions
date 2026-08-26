class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        topKL = [[] for i in range(len(nums) + 1)]

        for key, v in freq.items():
            topKL[v].append(key)
        res = []
        for i in range(len(topKL) - 1, -1, -1):
            for val in topKL[i]:
                res.append(val)
                if len(res) == k:
                    return res