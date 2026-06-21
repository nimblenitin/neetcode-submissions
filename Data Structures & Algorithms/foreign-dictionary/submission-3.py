class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            wMin = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:wMin] == w2[:wMin]:
                return ""
            for j in range(wMin):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        res = []
        visit = {}
        def dfs(char):
            if char in visit:
                return visit[char]
            visit[char] = True
            for nei in adj[char]:
                if dfs(nei):
                    return True
            res.append(char)
            visit[char] = False
    
            
        for char in adj:
            if dfs(char):
                return ""
        res.reverse()
        return "".join(res)