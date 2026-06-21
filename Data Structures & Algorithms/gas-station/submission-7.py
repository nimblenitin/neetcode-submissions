class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0 
        tot = 0

        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            tot += (gas[i] - cost[i])

            if tot < 0:
                tot = 0
                start = i + 1
        return start