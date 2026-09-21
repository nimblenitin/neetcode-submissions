class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)

        adj = defaultdict(list)

        for w in wordList:
            for i in range(len(w)):
                pat = w[:i] + "*" + w[i + 1:]
                adj[pat].append(w)
        
        q = deque()
        res = 1
        q.append(beginWord)
        visit = set()
        visit.add(beginWord)

        while q:
            for i in range(len(q)):
                w1 = q.popleft()
                if w1 == endWord:
                    return res
                for j in range(len(w1)):
                    pat = w1[:j] + "*" + w1[j + 1:]
                    for w2 in adj[pat]:
                        if w2 not in visit:
                            q.append(w2)
                            visit.add(w2)
            res += 1
        return 0

