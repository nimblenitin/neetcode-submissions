class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inToNumHaSet = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in inToNumHaSet:
                return [inToNumHaSet[diff], i]
            inToNumHaSet[num] = i