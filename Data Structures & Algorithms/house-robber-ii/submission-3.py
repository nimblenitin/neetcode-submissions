class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.helper(nums[1:]), self.helper(nums[:-1]), nums[0])
    
    def helper(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max((num + rob1), rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        