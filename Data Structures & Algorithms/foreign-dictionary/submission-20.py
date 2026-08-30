class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        order = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for i in range(minLen):
                if w1[i] != w2[i]:
                    order[w1[i]].add(w2[i])
                    break
        visit = {}
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for dep in order[c]:
                if dfs(dep):
                    return True
            res.append(c) 
            visit[c] = False
            return False
        
        for c in order:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)


            