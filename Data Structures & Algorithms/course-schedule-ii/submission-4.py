class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for course, depen in prerequisites:
            adj[course].append(depen)
        
        cycle = set()
        visited = set()
        res = []

        def dfs(cou):
            if cou in cycle:
                return False
            if cou in visited:
                return True
            cycle.add(cou)
            for dep in adj[cou]:
                if not dfs(dep):
                    return False
            visited.add(cou)
            res.append(cou)
            cycle.remove(cou)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res