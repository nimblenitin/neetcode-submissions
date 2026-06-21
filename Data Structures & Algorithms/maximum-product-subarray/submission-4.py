class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = nums[0]
        for num in nums:
            tmpMax = num * curMax
            curMax = max(num, num * curMax, num * curMin)
            curMin = min(num, tmpMax, num * curMin)
            res = max(res, curMax)
        return res 
