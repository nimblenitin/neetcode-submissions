class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i + 1:]
                adj[pat].append(word)

        q = collections.deque()
        res = 1
        q.append(beginWord)
        visit = set()
        visit.add(beginWord)
        while q:
            for i in range(len(q)):
                word = q.popleft()   
                if word == endWord:
                    return res 
                for j in range(len(word)):
                    pat = word[:j] + "*" + word[j + 1:]
                    for word2 in adj[pat]:
                        if word2 not in visit:
                            visit.add(word2)
                            q.append(word2)
            res += 1
        return 0
                