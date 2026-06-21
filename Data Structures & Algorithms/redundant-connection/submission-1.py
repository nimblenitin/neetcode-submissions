class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(node):
            if node != par[node]:
                par[node] = find(par[node])
            return par[node]

        def union(n1, n2):
            r1 = find(n1)
            r2 = find(n2)
            if r1 == r2:
                return False
            if rank[r1] > rank[r2]:
                par[r2] = r1
                rank[r1] += rank[r2]
            else:
                par[r1] = r2
                rank[r2] += rank[r1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
