class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        depMap = {i: [] for i in range(numCourses)}
        seen, cycle = set(), set()
        res = []

        for co, pre in prerequisites:
            depMap[co].append(pre)

        def dfs(co):
            if co in cycle:
                return False
            
            if co in seen:
                return True

            cycle.add(co)
            for dep in depMap[co]:
                if not dfs(dep):
                    return False
            cycle.remove(co)
            seen.add(co)
            res.append(co)
            return True
            

        for co in range(numCourses):
            if not dfs(co):
                return []
        return res