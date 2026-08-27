class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}

        for n in nums:
            freqDict[n] = freqDict.get(n, 0) + 1
        
        freqList = [[] for _ in range(len(nums) + 1)]

        for num, fre in freqDict.items():
            freqList[fre].append(num)

        res = []
        for i in range(len(nums), -1, -1):
            for val in freqList[i]:
                res.append(val)
                if len(res) == k:
                    return res

