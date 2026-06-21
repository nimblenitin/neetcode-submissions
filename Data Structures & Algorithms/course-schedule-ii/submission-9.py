class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)
        visit, cycle = set(), set()
        output = []
        def dfs(cou):
            if cou in visit:
                return True
            
            if cou in cycle:
                return False
            
            cycle.add(cou)

            for dep in adj[cou]:
                if not dfs(dep):
                    return False
                
            cycle.remove(cou)
            visit.add(cou)
            output.append(cou)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output