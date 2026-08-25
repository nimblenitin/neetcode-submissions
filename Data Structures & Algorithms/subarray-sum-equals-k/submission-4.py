class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ways = 0
        sumCount = {0: 1}
        tot = 0
        for n in nums:
            tot += n

            if (tot - k) in sumCount:
                ways += sumCount[tot - k]
            
            sumCount[tot] = 1 + sumCount.get(tot, 0)
        return ways