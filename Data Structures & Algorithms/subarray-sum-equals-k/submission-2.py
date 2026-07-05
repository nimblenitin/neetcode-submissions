class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        waysToSum = {0: 1}
        curSum = 0
        for n in nums:
            curSum += n
            diff = curSum - k
            res += waysToSum.get(diff, 0)
            waysToSum[curSum] = 1 + waysToSum.get(curSum, 0)
        return res