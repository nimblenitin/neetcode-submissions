class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        def dfs(i):
            if i >= len(nums):
                res.append(perm.copy())
                return
            perm.append(nums[i])
            dfs(i + 1)

            perm.pop()
            dfs(i + 1)
        dfs(0)
        return res
