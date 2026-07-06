class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tot = 0
        totSet = {0: 1}
        ways = 0
        for n in nums:
            tot += n
            diff = (tot - k)
            if diff in totSet:
                ways += totSet.get(diff, 0)
            totSet[tot] = 1 + totSet.get(tot, 0)
        return ways