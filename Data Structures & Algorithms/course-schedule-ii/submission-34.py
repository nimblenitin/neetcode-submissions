class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for c, d in prerequisites:
            adj[c].append(d)
            
        op = []
        visit = set()
        cycle = set()

        def dfs(i):
            if i in visit:
                return True
            
            if i in cycle:
                return False
            
            
            cycle.add(i)
            for dep in adj[i]:
                if not dfs(dep):
                    return False
            cycle.remove(i)
            op.append(i)
            visit.add(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return op