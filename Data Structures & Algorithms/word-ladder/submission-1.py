class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pat = word[:j] + "*" + word[j + 1:]
                adj[pat].append(word)
        q = collections.deque()
        q.append(beginWord)
        res = 1
        visit = set()
        visit.add(beginWord)
        while q:
            for i in range(len(q)):
                curWord = q.popleft()
                if curWord == endWord:
                    return res
                for j in range(len(curWord)):
                    pat = curWord[:j] + "*" + curWord[j + 1:]
                    for nei in adj[pat]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            res += 1
        return 0

                

        