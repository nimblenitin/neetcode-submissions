class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)
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
        dsu = DSU(n + 1)
        for n1, n2 in edges:
            if not dsu.union(n1, n2):
                return [n1, n2]
        