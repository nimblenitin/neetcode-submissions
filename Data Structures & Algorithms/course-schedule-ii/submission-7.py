class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(numCourses)}

        for cou, pre in prerequisites:
            adj[cou].append(pre)

        output = []
        visit = set()
        cycle = set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for co in range(numCourses):
            if not dfs(co):
                return []
        return output