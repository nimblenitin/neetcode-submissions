class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        
        for c, d in prerequisites:
            adj[c].append(d)

        visit = set()
        def dfs(c):
            if c in visit:
                return False
            
            if adj[c] == []:
                return True
            
            visit.add(c)
            for de in adj[c]:
                if not dfs(de):
                    return False
            
            visit.remove(c)
            adj[c] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

