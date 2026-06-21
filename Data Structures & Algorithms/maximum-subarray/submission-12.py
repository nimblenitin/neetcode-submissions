class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxtot = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxtot = max(curSum, maxtot)
        return maxtot