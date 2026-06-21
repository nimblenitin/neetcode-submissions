class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(n1, n2):
            r1 = find(n1)
            r2 = find(n2)
            if r1 == r2:
                return False
                
            if rank[r1] > rank[r2]:
                r1, r2 = r2, r1
            
            parent[r1] = r2
            rank[r2] += rank[r1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
