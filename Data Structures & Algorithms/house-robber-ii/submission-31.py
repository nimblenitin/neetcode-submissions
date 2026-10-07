class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.fMax(nums[1:]), self.fMax(nums[:-1]))

        
    def fMax(self, vals):
        rob1 = rob2 = 0

        for n in vals:
            tmp = rob1 
            rob1 = max(n + rob2, rob1)
            rob2 = tmp
        return rob1