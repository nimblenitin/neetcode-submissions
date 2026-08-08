class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for c, d in prerequisites:
            adj[c].append(d)

        visit = set()
        def dfs(i):
            if adj[i] == []:
                return True
            if i in visit:
                return False
            
            visit.add(i)

            for dep in adj[i]:
                if not dfs(dep):
                    return False
            adj[i] = []
            visit.remove(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

