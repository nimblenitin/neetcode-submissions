class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for val, f in count.items():
            freq[f].append(val)
        res = []
        for i in range(len(freq)-1, 0 ,-1):
            for v in freq[i]:
                res.append(v)
                if len(res) == k:
                    return res

