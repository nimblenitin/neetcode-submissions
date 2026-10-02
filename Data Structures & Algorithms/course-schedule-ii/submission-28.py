class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        for c, d in prerequisites:
            adj[c].append(d)
        
        cycle, visit = set(), set()
        op = []
        def dfs(co):
            if co in cycle:
                return False
            
            if co in visit:
                return True
            
            cycle.add(co)

            for dep in adj[co]:
                if not dfs(dep):
                    return False
                
            visit.add(co)
            cycle.remove(co)
            op.append(co)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return op