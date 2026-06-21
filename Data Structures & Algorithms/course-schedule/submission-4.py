class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depMap = {i: [] for i in range(numCourses)}
        for co, pre in prerequisites:
            depMap[co].append(pre)
        visiting = set()

        def dfs(cour):
            if depMap[cour] == []:
                return True
            if cour in visiting:
                return False
            visiting.add(cour)
            for prereq in depMap[cour]:
                if not dfs(prereq):
                    return False
            visiting.remove(cour)
            depMap[cour] = []
            return True            
        
        for cour in range(numCourses):
            if not dfs(cour):
                return False
        return True
