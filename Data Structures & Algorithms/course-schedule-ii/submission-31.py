class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        for c, d in prerequisites:
            adj[c].append(d)

        visit = set()
        cycle = set()
        op = []
        def dfs(c):
            if c in cycle:
                return False
            
            if c in visit:
                return True
            
            cycle.add(c)

            for dep in adj[c]:
                if not dfs(dep):
                    return False
            
            visit.add(c)
            cycle.remove(c)
            op.append(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return op
