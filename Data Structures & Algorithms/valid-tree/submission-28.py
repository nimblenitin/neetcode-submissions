class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        if not n:
            return True
        
        adj = {i: [] for i in range(n)}

        for no, de in edges:
            adj[no].append(de)
            adj[de].append(no)

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
            
            return True

        return dfs(0, -1) and len(visited) == n 