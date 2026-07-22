class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        freqList = [[] for _ in range(len(nums) + 1)]

        for num, fre in freq.items():
            freqList[fre].append(num)
        res = []
        for i in range(len(nums), -1, -1):
            for n in freqList[i]:
                res.append(n)
                if len(res) == k:
                    return res