class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffToI = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in diffToI:
                return [diffToI[diff], i]
            diffToI[v] = i