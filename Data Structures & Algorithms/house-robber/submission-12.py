class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        for n in nums:
            tmp = rob1
            rob1 = max(rob2 + n, rob1)
            rob2 = tmp
        return rob1