class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, newNums):
        rob1 = rob2 = 0
        for n in newNums:
            temp = max(rob2, n + rob1)
            rob1 = rob2
            rob2 = temp
        return rob2