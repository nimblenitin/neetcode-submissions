class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)

        visit = set()

        def dfs(cou):
            if adj[cou] == []:
                return True

            if cou in visit:
                return False

            visit.add(cou)

            for dep in adj[cou]:
                if not dfs(dep):
                    return False
                
            visit.remove(cou)
            adj[cou] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
