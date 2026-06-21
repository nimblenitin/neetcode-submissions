class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for course, dep in prerequisites:
            adj[course].append(dep)
        
        visiting = set()
        def dfs(cou):
            if cou in visiting:
                return False
            if adj[cou] == []:
                return True
            visiting.add(cou)
            for dep in adj[cou]:
                if not dfs(dep):
                    return False
            visiting.remove(cou)
            adj[cou] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
             
