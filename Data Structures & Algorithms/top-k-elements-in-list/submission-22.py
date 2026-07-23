class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        freqL = [[] for _ in range(len(nums) + 1)]

        for key, val in freq.items():
            freqL[val].append(key)
        res = []
        for i in range(len(nums), -1, -1):
            for num in freqL[i]:
                res.append(num)
                if len(res) == k:
                    return res
            