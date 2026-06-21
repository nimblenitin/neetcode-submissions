class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            dpT = set()
            for val in dp:
                if nums[i] + val == target or val == target:
                    return True
                dpT.add(val)
                dpT.add(nums[i] + val)
            dp = dpT
        return False 