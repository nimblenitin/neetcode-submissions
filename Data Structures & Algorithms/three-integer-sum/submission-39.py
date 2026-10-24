class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                tot = nums[l] + nums[r] + a 
                if tot > 0:
                    r -= 1
                elif tot < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1               
        return res

