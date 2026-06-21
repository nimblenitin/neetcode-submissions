class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pat = word[:j] + "*" + word[j + 1:]
                adj[pat].append(word)
        
        q = collections.deque([beginWord])
        res = 1
        visit = set([beginWord])
        while q:
            for i in range(len(q)):
                curW = q.popleft()
                if curW == endWord:
                    return res
                for j in range(len(curW)):
                    pat = curW[:j] + "*" + curW[j + 1:]
                    for nei in adj[pat]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            res += 1
        return 0




                

        