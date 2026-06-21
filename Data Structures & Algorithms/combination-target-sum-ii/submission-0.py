class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, cur, sum):
            if sum == target:
                res.append(cur.copy())
                return
            if i == len(candidates) or sum > target:
                return
            cur.append(candidates[i])
            dfs(i + 1, cur, sum + candidates[i])
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, sum) 
        dfs(0, [], 0)
        return res           