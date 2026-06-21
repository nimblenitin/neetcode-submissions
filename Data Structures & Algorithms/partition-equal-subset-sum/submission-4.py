class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            tempDp = set()
            for v in dp:
                if v + nums[i] == target:
                    return True
                tempDp.add(nums[i] + v)
                tempDp.add(v)
            dp = tempDp
        return False 