class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxS, curS = nums[0], 0
        for num in nums:
            if curS < 0:
                curS = 0
            curS += num
            maxS = max(maxS, curS)
        return maxS