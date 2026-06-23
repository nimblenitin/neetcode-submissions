class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minW = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minW] == w2[:minW]:
                return ""

            for i in range(minW):
                if w1[i] != w2[i]:
                    adj[w1[i]].add(w2[i])
                    break
        visit = {}
        res = []
        def dfs(char):
            if char in visit:
                return visit[char]

            visit[char] = True
            for nei in adj[char]:
                if dfs(nei):
                    return True
            
            visit[char] = False
            res.append(char)


        for char in adj:
            if dfs(char):
                return ""
        res.reverse()
        return "".join(res)

