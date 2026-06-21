class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in unique:
                length = 1
                while (length + num) in unique:
                    length += 1
                longest = max(longest, length)
        return longest