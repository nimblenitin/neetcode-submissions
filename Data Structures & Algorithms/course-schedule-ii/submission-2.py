class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        depMap = {i: [] for i in range(numCourses)}
        for course, depen in prerequisites:
            depMap[course].append(depen)
        visited = set()
        output = []
        cycle = set()
        def dfs(cou):
            if cou in visited:
                return True
            if cou in cycle:
                return False
            cycle.add(cou)
            for dep in depMap[cou]:
                if not dfs(dep):
                    return False
            cycle.remove(cou)
            visited.add(cou)
            output.append(cou)
            return True
        
        for cour in range(numCourses):
            if not dfs(cour):
                return []
        return output