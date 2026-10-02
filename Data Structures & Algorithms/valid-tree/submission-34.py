class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False

        adj = [[] for _ in range(n)]

        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        visit = set()
        def dfs(n, prev):
            if n in visit:
                return False
            
            visit.add(n)

            for dep in adj[n]:
                if dep == prev:
                    continue
                if not dfs(dep, n):
                    return False
                
            return True
        
        return dfs(0, -1) and len(visit) == n