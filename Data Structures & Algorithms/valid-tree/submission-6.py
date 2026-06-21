class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        adj = [[] for _ in range(n)]
        for value, depen in edges:
            adj[value].append(depen)
            adj[depen].append(value)
        visit = set()

        def dfs(val, prev):
            if val in visit:
                return False
            visit.add(val)
            for dep in adj[val]:
                if dep == prev:
                    continue
                else:
                    if not dfs(dep, val):
                        return False
            return True
        return dfs(0, -1) and len(visit) == n
        




