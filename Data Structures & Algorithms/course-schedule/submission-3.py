class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i: [] for i in range(numCourses)}
        for cour, prereq in prerequisites:
            preReq[cour].append(prereq)
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if preReq[course] == []:
                return True
            visiting.add(course)
            for pre in preReq[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            preReq[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
