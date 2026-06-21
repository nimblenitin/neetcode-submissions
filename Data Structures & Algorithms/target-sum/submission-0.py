class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def backtrack(i, currSum):
            
            if i == len(nums):
                return 1 if currSum == target else 0
            # if (i, currSum) in cache:
            #     return cache[(i, currSum)]
            
            return ((backtrack(i + 1, currSum + nums[i])
            + backtrack(i + 1, currSum - nums[i]))
)           
            # return cache[(i, currSum)]
        return backtrack(0, 0)