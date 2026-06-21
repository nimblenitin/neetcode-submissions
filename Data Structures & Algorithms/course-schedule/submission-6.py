class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depMap = {i: [] for i in range(numCourses)}
        for co, pre in prerequisites:
            depMap[co].append(pre)
        
        visit = set()
        
        def dfs(cou):
            if cou in visit:
                return False
            if depMap[cou] == []:
                return True
            visit.add(cou)
            for pr in depMap[cou]:
                if not dfs(pr):
                    return False
            visit.remove(cou)
            depMap[cou] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
             
