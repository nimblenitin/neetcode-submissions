class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for i in range(minLen):
                if w1[i] != w2[i]:
                    adj[w1[i]].add(w2[i])
                    break
        
        visit = {}
        res = []
        def dfs(char):
            if char in visit:
                return visit[char]
            visit[char] = True
            for nxtC in adj[char]:
                if dfs(nxtC):
                    return True
            visit[char] = False
            res.append(char)

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)

            
