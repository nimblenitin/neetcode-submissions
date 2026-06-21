class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        waysToReachDiff = {0: 1}
        curSum = 0
        for n in nums:
            curSum += n
            diff = curSum - k
            res += waysToReachDiff.get(diff, 0)
            waysToReachDiff[curSum] = waysToReachDiff.get(curSum, 0) + 1
        return res
