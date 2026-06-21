class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True

            if src not in adj:
                return False
            
            copy = list(adj[src])
            for i, v in enumerate(copy):
                res.append(v)
                adj[src].pop(i)
                if dfs(v):
                    return True
                adj[src].insert(i, v)
                res.pop()
            return False
        
        dfs("JFK") 
        return res    



            
