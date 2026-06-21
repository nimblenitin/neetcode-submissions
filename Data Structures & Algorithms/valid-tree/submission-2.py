class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False
        adj = [[] for _ in range(n)]
        for val, dep in edges:
            adj[val].append(dep)
            adj[dep].append(val)
        visit = set()
        def dfs(value, prev):
            if value in visit:
                return False
            visit.add(value)
            for depen in adj[value]:
                if depen == prev:
                    continue
                else:
                    if not dfs(depen, value):
                        return False
            return True
        
        return dfs(0, -1) and len(visit) == n




