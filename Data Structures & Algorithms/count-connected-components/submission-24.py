class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, n):
        cur = n
        while cur != self.par[cur]:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur] 
        return cur

    def merge(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)
        if r1 == r2:
            return False
        if self.rank[r1] > self.rank[r2]:
            r1, r2 = r2, r1
        self.par[r1] = r2
        self.rank[r2] += self.rank[r1]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n

        for n1, n2 in edges:
            res -= dsu.merge(n1, n2)
        return res