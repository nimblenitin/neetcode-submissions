class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)
        visit, cycle = set(), set()
        output = []
        def dfs(n):
            if n in visit:
                return True 
            
            if n in cycle:
                return False

            cycle.add(n)

            for nei in adj[n]:
                if not dfs(nei):
                    return False
            
            cycle.remove(n)
            visit.add(n)
            output.append(n)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
