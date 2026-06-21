class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToI = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in numToI:
                return [numToI[diff], i]
            numToI[v] = i