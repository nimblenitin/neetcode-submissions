class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for s, d in prerequisites:
            adj[s].append(d)
        
        visit = set()
        def dfs(co):
            if co in visit:
                return False
            
            if adj[co] == []:
                return True
            
            visit.add(co)

            for dep in adj[co]:
                if not dfs(dep):
                    return False
            
            adj[co] = []
            visit.remove(co)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True