class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, comb, tot):
            if tot == target:
                res.append(comb.copy())
                return
            
            if tot > target or i >= len(candidates):
                return

            comb.append(candidates[i])
            dfs(i + 1, comb, tot + candidates[i])

            comb.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, comb, tot)

        dfs(0, [], 0)
        return res