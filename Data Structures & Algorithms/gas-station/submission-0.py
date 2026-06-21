class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = 0
        count = 0
        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            count += gas[i] - cost[i]
            if count < 0:
                count = 0
                res = i + 1
        return res 
            
