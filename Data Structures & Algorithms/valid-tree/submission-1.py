class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        depMap = [[] for _ in range(n)]
        for val, dep in edges:
            depMap[val].append(dep)
            depMap[dep].append(val)
        visit = set()
        def dfs(value, prev):
            if value in visit:
                return False
            visit.add(value)
            for dep in depMap[value]:
                if dep == prev:
                    continue
                else:
                    if not dfs(dep, value):
                        return False
            return True
        return dfs(0, -1) and len(visit) == n



