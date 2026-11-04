class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freqL = [[] for _ in range(len(nums) + 1)]

        for v, f in freq.items():
            freqL[f].append(v)
        
        res = []
        for i in range(len(freqL) - 1, -1, -1):
            for val in freqL[i]:
                res.append(val)
                if len(res) == k:
                    return res