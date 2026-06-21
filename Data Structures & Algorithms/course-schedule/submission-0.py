class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depMap = {i:[] for i in range(numCourses)}
        seen = set()
        
        for co, dep in prerequisites:
            depMap[co].append(dep)

        def dfs(co):
            if co in seen:
                return False
            
            if depMap[co] == []:
                return True

            seen.add(co)
            for dep in depMap[co]:
                if not dfs(dep):
                    return False
            seen.remove(co)
            depMap[co] = []
            return True 
        
        for co in range(numCourses):
            if not dfs(co):
                return False
        return True