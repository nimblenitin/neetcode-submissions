class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for s, d in prerequisites:
            adj[s].append(d)

        visit = set()
        def dfs(i):
            if i in visit:
                return False
            
            if adj[i] == []:
                return True
            visit.add(i)

            for dep in adj[i]:
                if not dfs(dep):
                    return False
            visit.remove(i)
            adj[i] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True