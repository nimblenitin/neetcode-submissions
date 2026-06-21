class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        maxLen = curLen = 0
        for num in unique:
            if (num - 1) not in unique:
                curLen = 1
                while num + curLen in unique:
                    curLen += 1
                maxLen = max(maxLen, curLen)
        return maxLen
