class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)

            for dep in adj[i]:
                if dep == prev:
                    continue
                
                if not dfs(dep, i):
                    return False
            visited.add(i)
            return True
        
        return dfs(0, -1) and len(visited) == n


