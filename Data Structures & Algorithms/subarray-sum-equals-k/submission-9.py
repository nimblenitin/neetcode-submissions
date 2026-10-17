class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tot = {0: 1}
        cTot = 0
        ways = 0
        for n in nums:
            cTot += n
            if cTot - k in tot:
                ways += tot[cTot - k] 
            tot[cTot] = tot.get(cTot, 0) + 1
        return ways