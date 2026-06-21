class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, n1, n2):
        r1 = self.find(n1)
        r2 = self.find(n2)
        if r1 == r2:
            return False
        if self.rank[r1] > self.rank[r2]:
            r1, r2 = r2, r1
        self.parent[r1] = r2
        self.rank[r2] += self.rank[r1]
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)
        for n1, n2 in edges:
            if not dsu.union(n1, n2):
                return [n1, n2]
        
        
        