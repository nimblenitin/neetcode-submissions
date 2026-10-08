class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.maxP(nums[1:]), self.maxP(nums[:-1]))
    def maxP(self, hou):
        rob1 = rob2 = 0
        for n in hou:
            tmp = max(rob1, n + rob2)
            rob2 = rob1
            rob1 = tmp
        return rob1