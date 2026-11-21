class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for c, d in prerequisites:
            adj[c].append(d)
        visit = set()
        def dfs(c):
            if adj[c] == []:
                return True
            
            if c in visit:
                return False
            
            visit.add(c)
            for d in adj[c]:
                if not dfs(d):
                    return False
            
            adj[c] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


        