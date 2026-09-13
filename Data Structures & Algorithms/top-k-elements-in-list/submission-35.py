class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        freqList = [[] for _ in range(len(nums) + 1)]

        for key, v in freq.items():
            freqList[v].append(key)
        res = []
        for i in range(len(nums), -1, -1):
            for val in freqList[i]:
                res.append(val)
                if len(res) == k:
                    return res