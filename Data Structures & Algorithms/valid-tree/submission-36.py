class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        
        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(n, prev):
            if n in visit:
                return False
            
            visit.add(n)

            for d in adj[n]:
                if d == prev:
                    continue
                
                if not dfs(d, n):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n