class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        depMap = {i: [] for i in range(numCourses)}
        for co, dep in prerequisites:
            depMap[co].append(dep)
        output = []
        visited = set()
        visiting = set()
        def dfs(cou):
            if cou in visited:
                return True
            if cou in visiting:
                return False
            
            visiting.add(cou)
            for dep in depMap[cou]:
                if not dfs(dep):
                    return False
            visiting.remove(cou)
            visited.add(cou)
            output.append(cou)
            return True
        
        for cou in range(numCourses):
            if not dfs(cou):
                return []
        return output