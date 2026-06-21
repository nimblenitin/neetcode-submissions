class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin = curMax = 1
        for n in nums:
            if n == 0:
                curMin = curMax = 1
                continue
            temp = curMax * n
            curMax = max(n * curMin, n * curMax, n)
            curMin = min(n * curMin, temp, n)
            res = max(res, curMax)
        return res