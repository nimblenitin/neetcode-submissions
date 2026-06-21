class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        visit = set()
        for u, v in prerequisites:
            adj[u].append(v)

        def dfs(cou):
            if cou in visit:
                return False
            
            if adj[cou] == []:
                return True

            visit.add(cou)

            for nxt in adj[cou]:
                if not dfs(nxt):
                    return False
            
            visit.remove(cou)
            adj[cou] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True