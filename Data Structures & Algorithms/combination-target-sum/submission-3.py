class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, comb, tot):
            if tot == target:
                res.append(comb.copy())
                return
            
            if i >= len(nums) or tot >= target:
                return

            comb.append(nums[i])
            dfs(i, comb, tot + nums[i])
            comb.pop()

            dfs(i + 1, comb, tot)

        dfs(0, [], 0)
        return res