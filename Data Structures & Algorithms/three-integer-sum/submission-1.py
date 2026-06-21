class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, v in enumerate(nums):
            if v > 0:
                break
            if i > 0 and nums[i -1] == v:
                continue
            l, r = i + 1, len(nums) - 1
            sum = 0
            
            while l < r:
                sum = v + nums[l] + nums[r]
                if sum == 0:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        return res