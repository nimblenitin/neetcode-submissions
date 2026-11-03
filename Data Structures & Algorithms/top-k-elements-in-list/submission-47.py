class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) 
        freqL = [[] for i in range(len(nums) + 1)]

        for val, f in freq.items():
            freqL[f].append(val)
        res = []
        for i in range(len(freqL) - 1, -1, -1):
            for v in freqL[i]:
                res.append(v)
                if len(res) == k:
                    return res