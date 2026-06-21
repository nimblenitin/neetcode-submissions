class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        sum = 0
        idx_val = []
        n = len(nums)
        left, right = 0, n-1
        for i in range(n):
            req = target - nums[i]
            if req in seen:
                idx_val = [seen[req], i]
            seen[nums[i]] = i
        return idx_val