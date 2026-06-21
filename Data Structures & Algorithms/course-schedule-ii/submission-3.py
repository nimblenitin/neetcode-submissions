class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        depMap = {i: [] for i in range(numCourses)}
        for co, pr in prerequisites:
            depMap[co].append(pr)
        cycle = set()
        visited = set()
        res = []

        def dfs(cou):
            if cou in cycle:
                return False
            if cou in visited:
                return True
            cycle.add(cou)
            for dep in depMap[cou]:
                if not dfs(dep):
                    return False
            visited.add(cou)
            res.append(cou)
            cycle.remove(cou)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res