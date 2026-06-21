class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        return max(self.helper(nums, 1, n), self.helper(nums, 0, n-1))
        
    def helper(self, values, start, end):
        rob1, rob2 = 0, 0
        for i in range(start, end):
            temp = max(values[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2