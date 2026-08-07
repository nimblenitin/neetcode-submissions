class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for pre, dep in prerequisites:
            adj[pre].append(dep)

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
            
            visit.remove(i)
            adj[i] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True