class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        max_len = 0
        for i in range(len(nums)):
            length = 0
            if nums[i] - 1 not in numsset:
                while nums[i] + length in numsset:
                    length += 1
                max_len = max(max_len, length)
        return max_len
            
