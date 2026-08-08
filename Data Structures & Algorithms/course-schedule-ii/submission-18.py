class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        for c, d in prerequisites:
            adj[c].append(d)

        visit, cycle = set(), set()
        output = []

        def dfs(i):
            if i in cycle:
                return False
            
            if i in visit:
                return True
            
            cycle.add(i)
            
            for dep in adj[i]:
                if not dfs(dep):
                    return False
            output.append(i)
            visit.add(i)
            cycle.remove(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output

            
