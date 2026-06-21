class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i: [] for i in range(numCourses)}
        for co, pre in prerequisites:
            preReq[co].append(pre)
        visiting = set()

        def possible(cour):
            if (cour) in visiting:
                return False
            if preReq[cour] == []:
                return True
            
            visiting.add(cour)
            for pr in preReq[cour]:
                if not possible(pr):
                    return False
            visiting.remove(cour)
            preReq[cour] = []
            return True


        for cour in range(numCourses):
            if not possible(cour):
                return False
        return True