class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)
        
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            
            if adj[crs] == []:
                return True
            
            visit.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            visit.remove(crs)
            adj[crs] = []
            return True
        
        for cou in range(numCourses):
            if not dfs(cou):
                return False
        return True

             
