class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        adj = [[] for _ in range(n)]
        for node, edge in edges:
            adj[node].append(edge)
            adj[edge].append(node)
        cycle = set()
        def dfs(nod, prev):
            if nod in cycle:
                return False
            cycle.add(nod)
            for edge in adj[nod]:
                if edge == prev:
                    continue
                else:
                    if not dfs(edge, nod):
                        return False
            return True
        
        return dfs(0, -1) and len(cycle) == n 
        




