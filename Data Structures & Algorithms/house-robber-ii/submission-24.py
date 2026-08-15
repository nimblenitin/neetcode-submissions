class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self, nNums):
        rob1 = rob2 = 0


        for n in nNums:
            tmp = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = tmp
        return rob2
    