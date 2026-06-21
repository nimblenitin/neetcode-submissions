class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        maxL = 0
        for num in nums:
            if (num - 1) not in unique:
                length = 1
                while (num + length) in unique:
                    length += 1
                maxL = max(maxL, length)
        return maxL