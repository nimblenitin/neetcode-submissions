class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        output = []

        for c, d in prerequisites:
            adj[c].append(d)

        visit, cycle = set(), set()
        def dfs(c):
            if c in visit:
                return True
            
            if c in cycle:
                return False
            
            cycle.add(c)
            for dep in adj[c]:
                if not dfs(dep):
                    return False
            visit.add(c)
            output.append(c)
            cycle.remove(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
            


        