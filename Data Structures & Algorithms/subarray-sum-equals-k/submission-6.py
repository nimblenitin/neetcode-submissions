class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totC = {0 : 1}
        ways = 0
        tot = 0
        for n in nums:
            tot += n
            if (tot - k) in totC:
                ways += totC[(tot - k)]
            totC[tot] = totC.get(tot, 0) + 1
        return ways